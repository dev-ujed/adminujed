<template>
    <div class="modal modal-overlay">
      <div class="base-modal__panel modal-groups__card">
        <div class="modal-groups__close-button">
            <button  @click="handleClose"><img src="/static/img/Icon x.png" alt="Icono cerrar"></button>
        </div>
        <div class="base-modal__heading" >
            <h2 class="modal__title">{{ materia.desc_materia}}</h2>
        </div>
          <div class="base-modal__container">
            <div class="base-modal__container-info">
                <p><span>Clave: </span>{{ info.info_materia[0].clave }}</p>
                <p><span>Horas: </span>{{ info.info_materia[0].horas }}</p>
                <p><span>Créditos: </span>{{ info.info_materia[0].creditos }}</p>
                <div v-if="info.info_materia[0].materias_encadenadas">
                    <p class="mt-5"><img src="/static/img/Icon link.png" alt="Icono Link"><span>Materias encadenadas</span></p>
                    <ul>
                        <li>{{ info.info_materia[0].materias_encadenadas }}</li>
                    </ul>
                </div>
            </div>
            <hr>
            <div class="base-modal__container-grupos">
                <div class="grupos-select">
                    <select v-model="selectedCiclo" class="select-field form-field" @change="obtenerGruposPorCiclo">
                        <option value="" disabled selected>-- Ciclos anteriores --</option>
                        <option v-for="ciclo in info.ciclos" :key="ciclo.cve_ciclo" :value="ciclo.cve_ciclo">{{ ciclo.desc_ciclo }}</option>
                    </select>
                </div>
                <p><span>Grupos asignados: </span>{{ gruposAsignados }} de {{ totalGrupos }}</p>
                <div class="grupos">
                    <div class="grupos__info" v-for="(grupo, index) in gruposMostrar" :key="index">
                        <div class="grupos__info--header">
                            <div><h1 class="grupos__title">Grupo {{ grupo.grupo }}</h1></div>
                            <div class="grupos__cupo">
                              <progress :id="'cupo-' + grupo.grupo" max="100" :class="getProgresoColor(grupo)" :value="(grupo.inscritos / grupo.cupo) * 100">{{ (grupo.inscritos / grupo.cupo * 100).toFixed(0) }}%</progress>
                                <label for="cupo">{{ grupo.inscritos >= grupo.cupo ? 'Lleno' : 'Cupo' }}</label>
                            </div>
                        </div>
                        <div class="grupos__info--body">
                            <p><img src="/static/img/Icon students.png" alt="Icon students">{{ grupo.inscritos }} de {{ grupo.cupo }} estudiantes</p>
                            <a href=""><img src="/static/img/Icon teacher.png" alt="Icon teacher">{{ grupo.nom_maestro }} <img class="icon-select" src="/static/img/Vectorb.png" alt="Selec"></a>
                        </div>
                    </div>
                </div>
            </div>
          </div>
      </div>
    </div>
  </template>
  
<script>
  export default {
    name: 'Modal',
  
    props: {
      materia: {
        type: Object,
        required: true
      },

      cve_carrera: {
        type: [String, Number],
        required: true
      },

      cve_plan: {
        type: [String, Number],
        required: true
      },
        
      info: {
        type: Object
      },
      ciclos: {
        type: Array,
        required: true 
      }
    },

    data(){
        return{
            selectedCiclo: "",
            grupos: [],
        }
    },

    computed: {
        gruposAsignados() {
            return this.info.grupos?.filter(g => g.nom_maestro !== 'Sin asignar').length || 0;
        },
        totalGrupos() {
            return this.info.grupos?.length || 0;
        },
        gruposMostrar() {
            return this.grupos.length > 0 ? this.grupos : this.info.grupos || [];
        },
    },
  
    methods: {
      getProgresoColor(grupo) {
        const porcentaje = (grupo.inscritos / grupo.cupo) * 100;
        if(porcentaje == 100){
          return 'progress-red';
        }
      },

      handleClose() {
        this.$emit('close');
      },

      obtenerGruposPorCiclo() {
        if(this.selectedCiclo){
                axios.get(`/admi/grupos-ciclos/${this.selectedCiclo}/${this.cve_carrera}/${this.info.info_materia[0].clave}/${this.cve_plan}`)
                .then(response => {
                    console.log("Grupos recibidos:", response.data);

                    this.grupos = Array.isArray(response.data.grupos) ? response.data.grupos : [];

                    console.log("Grupos asignados a this.grupos:", this.grupos);
                })
                .catch(error => {
                    console.error("Error al obtener los grupos:", error);
                });
            }
        }
    }
  };
</script>

  