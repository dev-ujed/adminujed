<template>
    <div class="db-heading--admin">
        <h1 class="db-heading--admin__title">Unidades académicas</h1>
    </div>
    <div class="section">
        <div class="container container--admin section--admin mb-16">
            <form action="" class="db-search-form">
                <div class="search-wrapper">
                    <input id="search-input" name="buscar" type="search" placeholder="Filtrar por nombre o siglas" class="form-field search-input">
                    <img class="search-icon" src="/static/img/filtro-icon.png" alt="Icon filtro">
                </div>
            </form>
        </div>
        <div class="container container--admin card-container">
            <div class="db-panel card" @click="detallesUndiad(1)">
                <div class="card__title">CCH</div>
                <div class="card__body">
                    <p class="card__title-large">Colegio de Ciencias y Humanidades</p>
                    <p class="card__sede">Sede Durango</p>
                </div>
            </div>
            <div class="db-panel card" @click="detallesUndiad(2)">
                <div class="card__title">ECT</div>
                <div class="card__body">
                    <p class="card__title-large">Escuela de Ciencias y Tecnologías</p>
                    <p class="card__sede">Sede Durango</p>
                </div>
            </div>
            <div class="db-panel card">
                <div class="card__title">EPD</div>
                <div class="card__body">
                    <p class="card__title-large">Escuela Preparatoria Diurna</p>
                    <p class="card__sede">Sede Durango</p>
                </div>
            </div>
            <div class="db-panel card">
                <div class="card__title">FAZ</div>
                <div class="card__body">
                    <p class="card__title-large">Facultad de Agricultura y Zootecnia</p>
                    <p class="card__sede">Sede Gómez Palacio</p>
                </div>
            </div>
            <div class="db-panel card" @click="detallesUndiad(3)">
                <div class="card__title">FCQ</div>
                <div class="card__body">
                    <p class="card__title-large">Facultad de Ciencias Químicas</p>
                    <p class="card__sede">Sede Durango</p>
                </div>
            </div>
            <div class="db-panel card">
                <div class="card__title">FCQ GP</div>
                <div class="card__body">
                    <p class="card__title-large">Facultad de Ciencias Químicas (G.P.)</p>
                    <p class="card__sede">sede Gómez Palacio</p>
                </div>
            </div>
            <div class="db-panel card">
                <div class="card__title">ICS</div>
                <div class="card__body">
                    <p class="card__title-large">Instituto de Ciencias Sociales</p>
                    <p class="card__sede">Sede Durango</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
		name: 'unidades',

        methods:{
            detallesUndiad(id){
                window.location.href = `${id}/`;
            }
        }
    }
</script>