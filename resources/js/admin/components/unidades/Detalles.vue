<template>
    <div class="db-heading--admin">
        <h1 class="db-heading--admin__title">{{ nombre_largo }}</h1>
    </div>
    <section class="container container--admin section">
        <p class="">Esta unidad tiene 4 horas académicas sin asignar.</p>
        <div class="programs-activos">
            <h1 class="programs__title">Programas activos</h1>
            <div class="programs__container">
                <div class="programs__titulos">
                    <p class="programs__titulos--title">Licenciatura</p>
                    <div class="programs__cards db-panel">
                        <p class="cards__carrera">Ingeniero en Ciencia de los Materiales <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                        <p class="cards__anio">2020</p>
                        <button class="btn btn--db-index btn-card">Ver</button>
                    </div>
                    <div class="programs__cards db-panel">
                        <p class="cards__carrera">Químico Biotecnólogo <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                        <p class="cards__anio">2008</p>
                        <button class="btn btn--db-index btn-card">Ver</button>
                    </div>
                    <div class="programs__cards db-panel">
                        <p class="cards__carrera">Químico Farmacéutico Biólogo <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                        <p class="cards__anio">2020</p>
                        <button class="btn btn--db-index btn-card">Ver</button>
                    </div>
                </div>

                <div class="programs__titulos">
                    <p class="programs__titulos--title">Maestría</p>
                    <div class="programs__cards db-panel">
                        <p class="cards__carrera">Maestría en Biología Molecular y Celular <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                        <p class="cards__anio">2018</p>
                        <button class="btn btn--db-index btn-card">Ver</button>
                    </div>
                    <div class="programs__cards db-panel">
                        <p class="cards__carrera">Maestría en Ciencias en Nanotecnología y Química de Materiales <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                        <p class="cards__anio">2018</p>
                        <button class="btn btn--db-index btn-card">Ver</button>
                    </div>
                </div>

                <div class="programs__titulos">
                    <p class="programs__titulos--title">Doctorado</p>
                    <div class="programs__cards db-panel">
                        <p class="cards__carrera">Doctorado en Ciencias Biomédicas <span><img src="/static/img/Vector.png" alt="ver mas"></span></p>
                        <p class="cards__anio">2020</p>
                        <button class="btn btn--db-index btn-card">Ver</button>
                    </div>
                </div>
            </div>
        </div>


        <div class="programs-inactivos">
            
        </div>
    </section>
</template>
<script>
    export default{
        name: 'detalles',
        data(){
            return{
                nombre_largo: '',
            }
        },

        mounted(){
            this.nombre_largo = document.getElementById('unidad-data').getAttribute('data-nombre-largo');
        }
    }
</script>