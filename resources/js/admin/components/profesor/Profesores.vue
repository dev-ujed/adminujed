<template>
    <div class="db-heading--admin">
        <h1 class="db-heading--admin__title">Profesores</h1>
    </div>
    <section class="section">
        <div class="container container--admin section--admin mb-16">
            <form @submit.prevent="handleSearch" class="db-search-form">
                <div class="search-wrapper">
                    <input id="search-input" v-model="searchQuery" name="buscar" type="search" placeholder="Buscar por matrícula o nombre" class="form-field search-input" @keyup.enter="handleSearch">
                    <img src="/static/img/Icon search.png" alt="Buscar" class="search-icon">
                </div>
            </form>
        </div>
        <div class="container container--admin">
            
            <p class="" v-if="totalResults > 0">Se encontraron {{ totalResults }} registros para “{{ searchQuery }}”.</p>

            <div class="db-panel-p">
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Matrícula</th>
                                <th>Nombre</th>
                                <th>Unidades académicas</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="profesor in profesores" :key="profesor.pl_matricula" class="record">
                                <td>{{ profesor.pl_matricula }}</td>
                                <td>{{ profesor.nom }}</td>
                                <td>
                                    <div class="unidad-academica">{{ profesor.escuela_nombre }}</div>
                                </td>
                                <td><a :href="`/admi/profesor/${profesor.pl_matricula}/`" class="btn btn--db-index">Ver</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="list-container">
                    <div class="record" v-for="profesor in profesores" :key="profesor.pl_matricula">
                        <a :href="`/admi/profesor/${profesor.pl_matricula}/`" class="record__name"><strong>{{ profesor.nom }} <span><img src="/static/img/Vector.png" alt="ver mas"></span></strong></a>
                        <div class="record__contaier">
                            <div class="record__container--sub title">
                                <p>{{ profesor.pl_matricula }} </p>
                                <p>{{ profesor.escuela_nombre }}</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <nav role="navegation" class="pagination-container">
                    <ul class="pagination pagination--dashboard">
                        <li v-for="page in visiblePages" :key="page">
                            <button 
                                class="pagination-item"
                                :class="{ 'pagination-item--selected': currentPage === page }"
                                @click="changePage(page)"
                                :disabled="currentPage === page"
                            >{{ page }}</button>
                        </li>
                        <li>
                            <button class="pagination-next" @click="changePage('next')">
                                <span class="pagination-next__icon"><span class="pagination-next__text">Siguiente</span><img src="/static/img/Vector.png" alt="icon next"></span>
                            </button>
                        </li>
                    </ul>
                    <div class="pagination--responsive">
                        <button class="pagination-previous pagination-previous--disabled" @click="goToPreviousPage" :class="{ 'pagination-previous--disabled': !hasPreviousPage }"><span class="pagination-previous__icon mr-1"><img src="/static/img/icon-prev.png" alt="prev"></span></button>
                        <div class="pagination-pages">
                            <select name="pagination" id="pagination" class="form-field-p" v-model="currentPage">
                                <option v-for="page in totalPages" :key="page" :value="page">{{ page }}</option>
                            </select>
                            <span>de {{ totalPages }}</span>
                        </div>
                        <button type="button" rel="next" class="pagination-next" @click="goToNextPage" :class="{ 'pagination-next--disabled': !hasNextPage }"><span class="pagination-next__icon"><img src="/static/img/icon-next.png" alt="next"></span></button>
                    </div>
                </nav>
            </div>
        </div>
    </section>
</template>
<script>

    import axios from 'axios';

    export default {
		name: 'profesores',
        data(){
            return{
                searchQuery: '',
                profesores: [],
                currentPage: 1,
                totalPages: 1,
                hasNextPage: true,
                hasPreviousPage: true,
                visiblePages: [],
                totalResults: '',
            }
        },

        computed: {
            
        },

        watch: {
            currentPage(newPage, oldPage){
                if(newPage !== oldPage){
                    this.getInfoProfes();
                }
            }
        },

        methods:{
            async handleSearch() {
                try {
                    const response = await axios.get(`info/`, {
                        params: {
                            search: this.searchQuery,
                            page: this.currentPage
                        }
                    });

                    this.profesores = response.data.profesores;
                    this.totalPages = response.data.total_pages;
                    this.currentPage = response.data.current_page;
                    this.totalResults = response.data.total_results;
                } catch (error) {
                    console.error("Error al buscar profesores:", error);
                }
            },

            getInfoProfes(query = '') {
                axios.get('info/', { 
                    params: { 
                        page: this.currentPage, 
                        buscar: query 
                    }
                })
                .then(response => {
                    console.log('Respuesta de la API: ', response.data);
                    this.profesores = response.data.profesores;
                    this.totalPages = response.data.total_pages;
                    this.currentPage = response.data.current_page;
                    this.hasNextPage = response.data.has_next;
                    this.hasPreviousPage = response.data.has_previous;

                    this.updateVisiblePages();
                })
                .catch(error => {
                    console.log(error);
                });
            },

            changePage(page) {
                if (page === 'next' && this.currentPage < this.totalPages) {
                this.currentPage++;
                } else if (page === 'previous' && this.currentPage > 1) {
                    this.currentPage--;
                } else if (typeof page === 'number') {
                    this.currentPage = page;
                }

                this.getInfoProfes();
            },

            changePageMovile(){
                this.getInfoProfes();
            },

            updateVisiblePages() {
                let pages = [];
                const maxVisiblePages = 5;
                let startPage = Math.max(this.currentPage - Math.floor(maxVisiblePages / 2), 1);
                let endPage = Math.min(startPage + maxVisiblePages - 1, this.totalPages);

                if (endPage - startPage + 1 < maxVisiblePages) {
                    startPage = Math.max(endPage - maxVisiblePages + 1, 1);
                }

                for (let i = startPage; i <= endPage; i++) {
                    pages.push(i);
                }

                this.visiblePages = pages;
            },

            goToPreviousPage() {
                if (this.currentPage > 1) {
                    this.currentPage--;
                    this.getInfoProfes();
                }
            },

            goToNextPage() {
                if (this.currentPage < this.totalPages) {
                    this.currentPage++;
                    this.getInfoProfes();
                }
            },
        },

        mounted(){
            this.getInfoProfes();
        }
    }
</script>