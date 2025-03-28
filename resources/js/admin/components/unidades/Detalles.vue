<template>
    <div class="db-heading--admin">
        <h1 class="db-heading--admin__title">{{ nombreEscuela }}</h1>
    </div>
    <section class="container container--admin section">
        <p class="">Esta unidad tiene 4 horas académicas sin asignar.</p>

        <div v-if="esPreparatoria" class="">
            <h1 class="programs__title">Programas activos</h1>
            <div v-if="preparatorias.length === 0">
                <p>No hay programas disponibles para esta preparatoria.</p>
            </div>
            <div v-for="carrera in preparatoriasActivas" :key="carrera.cve_carrera" class="programs__cards db-panel">
                <p class="cards__carrera">{{ carrera.desc_carrera }} <span><img src="/static/img/Vector.png" alt="ver más"></span></p>
                <p class="cards__anio">{{ carrera.anio }}</p>
                <button class="btn btn--db-index btn-card">Ver</button>
            </div>

            <h1 class="programs__title">Programas inactivos</h1>
            <div v-if="preparatoriasInactivas.length === 0">
                <p>No hay programas inactivos para esta preparatoria.</p>
            </div>
            <div v-for="carrera in preparatoriasInactivas" :key="carrera.cve_carrera" class="programs__cards db-panel">
                <p class="cards__carrera">{{ carrera.desc_carrera }} <span><img src="/static/img/Vector.png" alt="ver más"></span></p>
                <p class="cards__anio">{{ carrera.anio }}</p>
                <button class="btn btn--db-index btn-card">Ver</button>
            </div>
        </div>

        <!-- Si no es prepa -->
        <div v-else>
            <div class="programs-activos">
                <h1 class="programs__title">Programas activos</h1>

                <!-- Licenciaturas Activas -->
                <div class="programs__container">
                    <div class="programs__titulos">
                        <p class="programs__titulos--title">Licenciatura</p>
                        <div v-if="licenciaturasActivas.length === 0">
                            <p>No hay programas activos de Licenciatura.</p>
                        </div>
                        <div class="programs__cards db-panel" v-for="carrera in licenciaturasActivas" :key="carrera.cve_carrera">
                            <p class="cards__carrera">{{ carrera.desc_carrera }} <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                            <p class="cards__anio">{{ carrera.anio }}</p>
                            <button class="btn btn--db-index btn-card">Ver</button>
                        </div>
                    </div>

                    <!-- Maestrías Activas -->
                    <div class="programs__titulos">
                        <p class="programs__titulos--title">Maestrías</p>
                        <div v-if="maestriasActivas.length === 0">
                            <p>No hay programas activos de Maestría.</p>
                        </div>
                        <div class="programs__cards db-panel" v-for="carrera in maestriasActivas" :key="carrera.cve_carrera">
                            <p class="cards__carrera">{{ carrera.desc_carrera }} <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                            <p class="cards__anio">{{ carrera.anio }}</p>
                            <button class="btn btn--db-index btn-card">Ver</button>
                        </div>
                    </div>

                    <!-- Doctorados Activos -->
                    <div class="programs__titulos">
                        <p class="programs__titulos--title">Doctorados</p>
                        <div v-if="doctoradosActivas.length === 0">
                            <p>No hay programas activos de Doctorado.</p>
                        </div>
                        <div class="programs__cards db-panel" v-for="carrera in doctoradosActivas" :key="carrera.cve_carrera">
                            <p class="cards__carrera">{{ carrera.desc_carrera }} <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                            <p class="cards__anio">{{ carrera.anio }}</p>
                            <button class="btn btn--db-index btn-card">Ver</button>
                        </div>
                    </div>
                </div>
            </div>

            <div class="programs-inactivos">
                <h1 class="programs__title">Programas inactivos</h1>

                <!-- Licenciaturas Inactivas -->
                <div class="programs__container">
                    <div class="programs__titulos">
                        <p class="programs__titulos--title">Licenciatura</p>
                        <div v-if="licenciaturasInactivas.length === 0">
                            <p>No hay programas inactivos de Licenciatura.</p>
                        </div>
                        <div class="programs__cards db-panel" v-for="carrera in licenciaturasInactivas" :key="carrera.cve_carrera">
                            <p class="cards__carrera">{{ carrera.desc_carrera }} <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                            <p class="cards__anio">{{ carrera.anio }}</p>
                            <button class="btn btn--db-index btn-card">Ver</button>
                        </div>
                    </div>

                    <!-- Maestrías Inactivas -->
                    <div class="programs__titulos">
                        <p class="programs__titulos--title">Maestrías</p>
                        <div v-if="maestriasInactivas.length === 0">
                            <p>No hay programas inactivos de Maestría.</p>
                        </div>
                        <div class="programs__cards db-panel" v-for="carrera in maestriasInactivas" :key="carrera.cve_carrera">
                            <p class="cards__carrera">{{ carrera.desc_carrera }} <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                            <p class="cards__anio">{{ carrera.anio }}</p>
                            <button class="btn btn--db-index btn-card">Ver</button>
                        </div>
                    </div>

                    <!-- Doctorados Inactivos -->
                    <div class="programs__titulos">
                        <p class="programs__titulos--title">Doctorados</p>
                        <div v-if="doctoradosInactivas.length === 0">
                            <p>No hay programas inactivos de Doctorado.</p>
                        </div>
                        <div class="programs__cards db-panel" v-for="carrera in doctoradosInactivas" :key="carrera.cve_carrera">
                            <p class="cards__carrera">{{ carrera.desc_carrera }} <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                            <p class="cards__anio">{{ carrera.anio }}</p>
                            <button class="btn btn--db-index btn-card">Ver</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>
<script>
    export default{
        name: 'detalles',
        props: ['carreras'],

        data(){
            return{
                carrerasData: this.carreras,
                nombreEscuela: '',
            }
        },
        computed:{
            esPreparatoria(){
                return this.carreras.some(carrera => {
                    const claveNum = Number(carrera.cve_carrera);
                    return claveNum >= 12000000 && claveNum <= 12000206;
                });
                //return this.carreras.every(carrera => carrera.cve_carrera >= '12000201' && carrera.cve_carrera <= '12000206');
            },
            preparatorias() {
                return this.carreras.filter(carrera => {
                    const claveNum = Number(carrera.cve_carrera);
                    return claveNum >= 12000000 && claveNum <= 12000206;
                });
                //return this.carreras.filter(carrera => carrera.cve_carrera >= '12000201' && carrera.cve_carrera <= '12000206');
            },

            preparatoriasActivas() {
                return this.preparatorias.filter(carrera => carrera.activa === 'S');
            },
            preparatoriasInactivas() {
                return this.preparatorias.filter(carrera => carrera.activa === 'N');
            },

            // Filtrar las carreras activas por tipo
            licenciaturasActivas() {
                return this.carreras.filter(carrera => carrera.activa === 'S' && carrera.cve_carrera >= '140000' && carrera.cve_carrera <= '149999');
            },
            maestriasActivas() {
                return this.carreras.filter(carrera => carrera.activa === 'S' && carrera.cve_carrera >= '160000' && carrera.cve_carrera <= '169999');
            },
            doctoradosActivas() {
                return this.carreras.filter(carrera => carrera.activa === 'S' && carrera.cve_carrera >= '170000' && carrera.cve_carrera <= '179999');
            },
            // Filtrar las carreras inactivas por tipo
            licenciaturasInactivas() {
                return this.carreras.filter(carrera => carrera.activa === 'N' && carrera.cve_carrera >= '140000' && carrera.cve_carrera <= '149999');
            },
            maestriasInactivas() {
                return this.carreras.filter(carrera => carrera.activa === 'N' && carrera.cve_carrera >= '160000' && carrera.cve_carrera <= '169999');
            },
            doctoradosInactivas() {
                return this.carreras.filter(carrera => carrera.activa === 'N' && carrera.cve_carrera >= '170000' && carrera.cve_carrera <= '179999');
            }
        },

        mounted(){
            this.nombreEscuela = localStorage.getItem('escuela_nombre');
        }
    }
</script>