<template>
    <div class="db-heading--admin">
        <h1 class="db-heading--admin__title">Unidades académicas</h1>
    </div>
    <div class="section">
        <div class="container container--admin section--admin mb-16">
            <form action="" class="db-search-form">
                <div class="search-wrapper">
                    <input id="search-input" v-model="searchQuery" name="buscar" type="search" placeholder="Filtrar por nombre o siglas" class="form-field search-input">
                    <img class="search-icon" src="/static/img/filtro-icon.png" alt="Icon filtro">
                </div>
            </form>
        </div>
        <div class="container container--admin card-container">
            <div class="db-panel card" v-for="escuela in filtrarEscuelas" :key="escuela.cve_escuela" @click="detallesUnidad(escuela.cve_escuela)">
                <div class="card__title">{{ escuela.desc_corto}}</div>
                <div class="card__body">
                    <p class="card__title-large">{{ escuela.desc_completo }}</p>
                    <p class="card__sede">Sede {{ escuela.ubicacion }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
		name: 'unidades',
        data(){
            return{
                escuelas: [],
                searchQuery: "",
            };
        },

        computed: {
            filtrarEscuelas() {
                if (!this.searchQuery.trim()) {  
                    return this.escuelas;
                }

                const query = this.searchQuery.trim().toUpperCase();

                return this.escuelas.filter(escuela => {
                    const nombre = escuela.desc_completo ? escuela.desc_completo.toUpperCase() : "";
                    const clave = escuela.cve_escuela ? String(escuela.cve_escuela).toUpperCase() : "";
                    const nombre_corto = escuela.desc_corto ? escuela.desc_corto.toUpperCase() : "";

                    return nombre.includes(query) || clave.includes(query) || nombre_corto.includes(query);
                });
            }
        },

        methods:{
            detallesUnidad(id){
                const nom_escuela = this.escuelas.find(esc => esc.cve_escuela === id);
                window.location.href = `/admi/carreras/${id}/`;
                localStorage.setItem('escuela_nombre', nom_escuela.desc_completo);
            },

            getEscuelas(){
                axios.get('unidades/')
                .then(response => {
                    this.escuelas = response.data;
                })
                .catch(error => {
                    console.log(error);
                })
            },
        },

        mounted(){
            this.getEscuelas();
        }
    }
</script>