<template>
    <div class="main main-admin">
        <div class="db-heading--admin">
            <h1 class="page-title">Profesores</h1>
        </div>
        <section class="section">
            <div class="container container--admin mb-16">
                <form action="" class="db-search">
                    <input id="search-input" name="buscar" type="search" placeholder="Buscar por matrícula o nombre" class="form-field db-search__input max-w-500">
                    <button type="submit" class="btn btn--db db-search__btn">
                        buscar
                    </button>
                </form>
            </div>
            <div class="container container--admin">
                <div class="db-panel">
                    <div class="db-panel__order mb-12">
                        <p class="">Se encontraron 37 registros para “Fernand”.</p>
                    </div>
                    <table class="table table-index table-index--full-w table-indez--mobile">
                        <thead>
                            <tr class="table-index__headings">
                                <th>Matrícula</th>
                                <th>Nombre</th>
                                <th>Unidades académicas</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="table-index__row">
                                <td>123456781</td>
                                <td>Abreu Fernández Carolina</td>
                                <td>Facultad de Derecho Facultad de Economía, Contaduría y Administración</td>
                                <td><span class="table-index__label"><a href="" class="btn btn--db-index">Ver</a></span></td>
                            </tr>
                            <tr class="table-index__row">
                                <td>123456783</td>
                                <td>Fernández Reyna Mario Alberto</td>
                                <td>Instituto de Ciencias Sociales</td>
                                <td><span class="table-index__label"><a href="" class="btn btn--db-index">Ver</a></span></td>
                            </tr>
                            <tr class="table-index__row">
                                <td>123456784</td>
                                <td>Navarro Pérez Fernando</td>
                                <td>Facultad de Medicina y Nutrición</td>
                                <td><span class="table-index__label"><a href="" class="btn btn--db-index">Ver</a></span></td>
                            </tr>
                            <tr class="table-index__row">
                                <td>123456782</td>
                                <td>Rodríguez Sandoval Juan Fernando</td>
                                <td>Facultad de Medicina Veterinaria y Zootecnia</td>
                                <td><span class="table-index__label"><a href="" class="btn btn--db-index">Ver</a></span></td>
                            </tr>
                        </tbody>
                    </table>
                    <nav role="navegation" class="pagination-container">
                        <ul class="pagination pagination--dashboard">
                            <li>
                                <button class="pagination-previous pagination-previous--disabled"><span class="pagination-previous__icon mr-1"><</span></button>
                            </li>
                            <li>
                                <button class="pagination-item pagination-item--selected">1</button>
                            </li>
                            <li>
                                <button class="pagination-item">2</button>
                            </li>
                            <li>
                                <button class="pagination-item">3</button>
                            </li>
                            <li>
                                <button class="pagination-next"><span class="pagination-next__icon">></span></button>
                            </li>
                        </ul>
                        <div class="pagination--responsive pagination--responsive__dashboard">
                            <button class="pagination-previous pagination-previous--disabled"><span class="pagination-previous__icon mr-1"><</span></button>
                            <div class="pagination-pages">
                                <select name="pagination" id="pagination" class="form-field mr-2">
                                    <option value="1">1</option>
                                    <option value="2">2</option>
                                    <option value="3">14</option>
                                </select>
                                <span class="nowrap">de 14</span>
                            </div>
                            <button type="button" rel="next" class="pagination-next"><span class="pagination-next__icon">></span></button>
                        </div>
                    </nav>
                </div>
            </div>
        </section>
    </div>
</template>
<script>
    export default {
		name: 'profesores',
    }
</script>