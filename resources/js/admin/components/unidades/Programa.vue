<template>
    <div>
        <div class="db-heading--admin">
            <h1 class="db-heading--admin__title"><span>{{ carreraNombre }}</span></h1>
        </div>
        <div v-if="planes_actuales.length > 0">
            <div class="section">
                <div class="container plan-container">
                    {{ ciclos }}
                    <div>
                        <select v-model="planSeleccionado" class="select-field form-field">
                            <option disabled value="">-- Selecciona un plan --</option>
                            <option v-for="plan in planes_actuales" :key="plan.cve_plan" :value="plan.cve_plan">
                                {{ plan.desc_plan }}
                            </option>
                        </select>
                    </div>
                </div>
            </div>
            <div class="container">
                <div class="db-panel">
                    <div class="db-panel__title"><p>Unidades de aprendizaje</p></div>

                    <div class="unidades-aprendizaje">
                        <div v-for="(materiasPorSemestre, semestre) in materias" :key="semestre" class="semestre">
                            <div class="semestre-title">SEMESTRE {{ semestre }}</div>
                            <ul class="materias-list">
                                <li v-for="materia in materiasPorSemestre" :key="materia.cve_materia" @click="abrirModal(materia)">
                                    {{ materia.desc_materia }}
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <modal v-if="modalVisible" :ciclos="ciclos" :materia="materiaSeleccionada" :cve_carrera="cve_carrera" :cve_plan="planSeleccionado" :info="materia_info" @close="cerrarModal" />
        </div>
        <div v-else class="section">
            <div class="container"><p>Sin planes activos</p></div>
        </div>


    </div>
</template>

<script>
    import axios from 'axios';
    import Modal from './Modal.vue';
    
    export default{
        name: "programa",

        components: {
            Modal
        },

        props: {
            cve_carrera: {
                type: [String, Number],
                required: true
            },

            planes_actuales:{
                type: [String, Number],
                required: true
            },

            ciclos: {
                type: [String, Number],
                required: true 
            },
        },

        data(){
            return{
                carreraNombre: '',
                planSeleccionado: '',
                materias: {},
                materia_info: [],
                modalVisible: false,
                materiaSeleccionada: null,
            }
        },

        watch:{
            planSeleccionado(newPlan) {
                if (newPlan) {
                    this.obtenerMaterias(newPlan);
                    //this.materiaInfo(newPlan, this.cve_carrera);
                }
            }
        },

        computed: {
            
        },

        methods:{
            obtenerMaterias(cve_plan) {
                axios
                    .get(`/admi/materias_plan/?cve_plan=${cve_plan}`)
                    .then(response => {
                        this.materias = response.data;
                    })
                    .catch(error => {
                        console.error("Error al obtener materias:", error);
                    });
            },

            materiaInfo(planSeleccionado, cve_carrera, cve_materia){

                axios
                    .get(`/admi/materia-info/`, { params: { plan: planSeleccionado, carrera: cve_carrera, cve_materia: cve_materia } })
                    .then(response =>{
                        this.materia_info = response.data;
                        //console.log(this.materia_info);
                        this.modalVisible = true;
                    })
                    .catch(error => {
                        console.error("Error al traer la info de la materia: ", error);
                    })
            },

            abrirModal(materia) {
                this.materiaSeleccionada = materia;
                this.materiaInfo(this.planSeleccionado, this.cve_carrera, materia.cve_materia);
            },

                cerrarModal() {
                this.modalVisible = false;
                this.materiaSeleccionada = null;
            }
            
        },

        mounted() {
            this.carreraNombre = localStorage.getItem('carrera_nombre') || 'Nombre no disponible';
            console.log("ciclos: " + this.ciclos);
            
        }
    }
</script>