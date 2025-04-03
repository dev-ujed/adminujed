<template>
    <div>
        <div class="db-heading--admin">
            <h1 class="db-heading--admin__title"><span>{{ carreraNombre }}</span></h1>
        </div>
        <div v-if="planes_actuales.length > 0">

            <div class="section">
                <div class="container plan-container">
                    <div>
                        <p>Selecciona un plan {{ planSeleccionado }}</p>
                        <select v-model="planSeleccionado" class="select-field form-field">
                            <option v-for="plan in planes_actuales" :key="plan.cve_plan" :value="plan.cve_plan">
                                {{ plan.cve_plan }}
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
                                <li v-for="materia in materiasPorSemestre" :key="materia.cve_materia">
                                    {{ materia.desc_materia }}
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

        </div>
        <div v-else class="section">
            <div class="container"><p>Sin planes activos</p></div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    
    export default{
        name: "programa",

        props: {
            cve_carrera: {
                type: [String, Number],
                required: true
            },

            planes_actuales:{
                type: [String, Number],
                required: true
            },
        },

        data(){
            return{
                carreraNombre: '',
                planSeleccionado: '',
                materias: {},
            }
        },

        watch:{
            planSeleccionado(newPlan) {
                if (newPlan) {
                    this.obtenerMaterias(newPlan);
                }
            }
        },

        methods:{
            obtenerMaterias(cve_plan) {
                axios
                    .get(`/admi/materias_plan/?cve_plan=${cve_plan}`)
                    .then(response => {
                        this.materias = response.data;
                        console.log(this.materias)
                    })
                    .catch(error => {
                        console.error("Error al obtener materias:", error);
                    });
            }
        },

        mounted() {

            this.carreraNombre = localStorage.getItem('carrera_nombre') || 'Nombre no disponible';
        }
    }
</script>