<template>
    <div class="db-heading--admin">
        <h1 class="db-heading--admin__title">{{ profesor.nom }}</h1>
    </div>
    <div class="section container info-profesor">
        <div class="db-panel max-h">
            <div class="header-profile">
                <div class="header-profile__container">
                    <div class="header-profile__avatar">
                        <img src="/static/img/icono-user.png" alt="Imagen de perfil">
                        <div class="header-profile__avatar--info">
                            <p>{{ profesor.nom }}</p>
                            <p class="color-primary-text">{{ profesor.pl_matricula }}</p>
                        </div>
                    </div>
                    <div class="header-profile__info">
                        <div class="header-profile__info--main">
                            <p class="profile-card__property-name mb-0">Correo institucional</p>
                            <p class="profile-card__property-value mb-6">{{ profesor.correo }}</p>
                            <p class="profile-card__property-name mb-0">Categoría</p>
                            <p class="profile-card__property-value mb-6">C3</p>
                            <p class="profile-card__property-name mb-0">Antiguedad general</p>
                            <p class="profile-card__property-value mb-6">8 años</p>
                            <p class="profile-card__property-name mb-0">Antiguedad académica</p>
                            <p class="profile-card__property-value mb-6">8 años</p>
                        </div>
                    </div>
                 </div>
            </div>
        </div>
        <div class="info-profesor__datos">
            <div class="db-panel">
                <div class="db-panel__title"><p>Contratos</p></div>
                <div class="contratos--movile">
                    <div class="contrato">
                        <div class="contrato__header">
                            <div class="contrato__icon" @click="toggleInfo">
                                <p @click="toggleInfoTabla"><img :src="buttonImage" alt="Ver más"></p>
                                <p>Facultad de derecho</p>
                            </div>
                            <div class="contrato__status_A"><p>Activo</p></div>
                        </div>

                        <div class="contrato__info">
                            <div class="contrato__info--more">
                                <p class="contrato__info--more__title">Pernanencia:</p>
                                <p class="contrato__info--more__data">Base</p>
                            </div>
                            <div class="contrato__info--more">
                                <p class="contrato__info--more__title">Nombramiento:</p>
                                <p class="contrato__info--more__data">Titular</p>
                            </div>
                            <div class="contrato__info--more">
                                <p class="contrato__info--more__title">Tipo:</p>
                                <p class="contrato__info--more__data">Académico</p>
                            </div>
                            <div class="contrato__info--more">
                                <p class="contrato__info--more__title">Dedicación:</p>
                                <p class="contrato__info--more__data">H/S/M</p>
                            </div>
                            <div class="contrato__info--more">
                                <p class="contrato__info--more__title">Fecha de inicio:</p>
                                <p class="contrato__info--more__data">01/09/2023</p>
                            </div>
                            <div class="contrato__info--more">
                                <p class="contrato__info--more__title">Fecha de término:</p>
                                <p class="contrato__info--more__data">N/A</p>
                            </div>
                            <div class="contrato__info--more">
                                <p class="contrato__info--more__title">Documentos:</p>
                                <p class="contrato__info--more__data">Ver contrato</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="contratos-table">
                    <table class="tabla">
                        <thead>
                            <tr>
                                <th>Unidad académica</th>
                                <th>Estado</th>
                                <th>Permanencia</th>
                                <th>Nombramiento</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Facultad de derecho</td>
                                <td><div class="contrato__status_A"><p>Activo</p></div></td>
                                <td>Base</td>
                                <td>Titular</td>
                                <td @click="toggleInfoTabla" class="table-button"><img :src="buttonImage" alt="Ver más">{{ buttonText }}</td>
                            </tr>
                            <tr v-show="showMoreInfo" class="more-info">
                                <td colspan="5">
                                    <div class="contrato__info">
                                        <div class="contrato__info--more">
                                            <p class="contrato__info--more__title">Tipo:</p>
                                            <p class="contrato__info--more__data">Académico</p>
                                        </div>
                                        <div class="contrato__info--more">
                                            <p class="contrato__info--more__title">Dedicación:</p>
                                            <p class="contrato__info--more__data">H/S/M</p>
                                        </div>
                                        <div class="contrato__info--more">
                                            <p class="contrato__info--more__title">Fecha de inicio:</p>
                                            <p class="contrato__info--more__data">01/09/2023</p>
                                        </div>
                                        <div class="contrato__info--more">
                                            <p class="contrato__info--more__title">Fecha de término:</p>
                                            <p class="contrato__info--more__data">N/A</p>
                                        </div>
                                        <div class="contrato__info--more">
                                            <p class="contrato__info--more__title">Documentos:</p>
                                            <p class="contrato__info--more__data">Ver contrato</p>
                                        </div>
                                    </div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="db-panel">
                <div class="db-panel__title"><p>Nombramientos</p></div>
                <div class="nombramientos--movile">
                    <div class="nombramiento">
                        <h1 class="nombramiento__title">Titular</h1>
                        <p class="nombramiento__fac">Facultad de Derecho</p>
                        <p class="nombramiento__fac">01/09/2023</p>
                        <a class="nombramiento__link" href=""><img src="/static/img/Icon pdf-flat.svg" alt="Icono pdf">Documento</a>
                    </div>
                    <div class="nombramiento">
                        <h1 class="nombramiento__title">Titular</h1>
                        <p class="nombramiento__fac">Facultad de Derecho</p>
                        <p class="nombramiento__fac">01/09/2023</p>
                        <a class="nombramiento__link" href=""><img src="/static/img/Icon pdf-flat.svg" alt="Icono pdf">Documento</a>
                    </div>
                </div>
                <div class="nombramientos-table">
                    <table>
                        <thead>
                            <tr>
                                <th>Nombramiento</th>
                                <th>Unidad académica</th>
                                <th>Fecha</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Titular</td>
                                <td>Facultad de Derecho</td>
                                <td>01/09/2023</td>
                                <td><a class="nombramiento__link" href=""><img src="/static/img/Icon pdf-flat.svg" alt="Icono pdf">Documento</a></td>
                            </tr>
                            <tr>
                                <td>Titular</td>
                                <td>Facultad de Derecho</td>
                                <td>01/09/2023</td>
                                <td><a class="nombramiento__link" href=""><img src="/static/img/Icon pdf-flat.svg" alt="Icono pdf">Documento</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="db-panel">
                <div class="db-panel__title"><p>Grados académicos</p></div>
                <div class="grados-academicos">
                    <div class="grados">
                        <div class="grados__title">Maestría</div>
                        <div class="grados__info">
                            <p>Maestría en Administración Pública</p>
                            <p>Universidad Juárez del Estado de Durango</p>
                            <p>Pasante</p>
                        </div>
                    </div>
                    <div class="grados">
                        <div class="grados__title">Licenciatura</div>
                        <div class="grados__info">
                            <p>Licenciatura en Administración</p>
                            <p>Universidad Juárez del Estado de Durango</p>
                            <p>2018</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="db-panel">
                <div class="db-panel__title"><p>Carga horaria</p></div>
                <div class="select plan-container">
                    <select v-model="selectedCiclo" class="select-field form-field" @change="loadCicloDetails">
                        <option value="" disabled selected>-- Ciclos anteriores --</option>
                        <option v-for="ciclo in ciclos" :key="ciclo.cve_ciclo" :value="ciclo.cve_ciclo">{{ ciclo.desc_ciclo }}</option>
                    </select>
                </div>
                <div class="carga-horaria--movile">
                    <div v-if="materiasMostrar.length > 0">
                        <div class="horario record" v-for="(materia, index) in materiasMostrar" :key="index">
                            <div class="horario__titles">
                                <h1>{{ materia.materia }}</h1>
                                <p><img src="/static/img/Icon-fac.svg" alt="icono faculdad">{{ materia.nombre_escuela_corto }}</p>
                            </div>
                            <div class="horario__info">
                                <div class="horario__info--more">
                                    <div class="horario__info--more__title"><p>Nivel</p></div>
                                    <div class="horario__info--more__data"><p>{{ materia.nivel }}</p></div>
                                </div>
                                <!--<div class="horario__info--more">
                                    <div class="horario__info--more__title"><p>Modalidad</p></div>
                                    <div class="horario__info--more__data"><p>Presencial</p></div>
                                </div>-->
                                <div class="horario__info--more">
                                    <div class="horario__info--more__title"><p>Horas semanales</p></div>
                                    <div class="horario__info--more__data"><p>{{ materia.horas_semanas }}</p></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <p v-else>Sin carga horario en este ciclo</p>
                </div>

                <div class="horarios-tabla">
                    <table v-if="materiasMostrar.length > 0">
                        <thead>
                            <tr>
                                <th>Unidad académica</th>
                                <th>Materia</th>
                                <th>Nivel</th>
                                <!--<th>Modalidad</th>-->
                                <th>Horas semanales</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(materia, index) in materiasMostrar" :key="index">
                                <td>{{ materia.nombre_escuela }}</td>
                                <td>{{ materia.materia }}</td>
                                <td>{{ materia.nivel }}</td>
                                <!--<td>{{ materia.modalidad }}</td>-->
                                <td>{{ materia.horas_semanas }}</td>
                            </tr>
                        </tbody>
                    </table>
                    <p v-else>Sin carga horario en este ciclo</p>
                </div>
            </div>
        </div>
    </div>
    
</template>
<script>

    export default{
        name: 'detalles-profesor',

        props: {
            profesor: Object,
            info_materias: Object,
            ciclos: {
                type: Array,
                required: true 
            }
        },

        data(){
            return{
                showMoreInfo: false,
                buttonImage: "/static/img/Btn more.svg",
                buttonText: 'Más',
                selectedCiclo: "",
                info_materias_ciclo: {},
            }
        },

        computed: {
            materiasMostrar() {
                return this.selectedCiclo ? this.info_materias_ciclo : this.info_materias;
            }
        },

        methods: {
            toggleInfo(event) {
                const contrato = event.currentTarget.closest('.contrato');
                contrato.classList.toggle('mostrar-info');
            },

            toggleInfoTabla() {
                this.showMoreInfo = !this.showMoreInfo;
                this.buttonImage = this.showMoreInfo ? "/static/img/minus-circle.svg" : "/static/img/Btn more.svg";
                this.buttonText = this.showMoreInfo ? "Menos" : "Más";
            },

            async loadCicloDetails() {
                if (!this.selectedCiclo) {
                    return;
                }
                try {
                    const response = await axios.get(`/admi/profesor/materias/${this.profesor.pl_matricula}/${this.selectedCiclo}`);
                    this.info_materias_ciclo = response.data;
                } catch (error) {
                    console.error('Error al cargar las materias:', error);
                }
            },

            cambiarCiclo(nuevoCiclo) {
                this.selectedCiclo = nuevoCiclo;
                this.loadCicloDetails();
            }

        
        }
    }
</script>