<template>
    <div class="db-heading--admin">
        <h1 class="db-heading--admin__title">Profesores</h1>
    </div>
    <section class="section">
        <div class="container container--admin section--admin mb-16">
            <form action="" class="db-search-form">
                <div class="search-wrapper">
                    <input id="search-input" name="buscar" type="search" placeholder="Buscar por matrícula o nombre" class="form-field search-input">
                    <img src="/static/img/Icon search.png" alt="Buscar" class="search-icon">
                </div>
            </form>
        </div>
        <div class="container container--admin">
            
            <p class="">Se encontraron 37 registros para “Fernand”.</p>

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
                            <tr>
                                <td>123456781</td>
                                <td>Abreu Fernández Carolina</td>
                                <td>
                                    <div class="unidad-academica">Facultad de Derecho</div>
                                    <div class="unidad-academica">Facultad de Economía, Contaduría y Administración</div>
                                </td>
                                <td><button class="btn btn--db-index">Ver</button></td>
                            </tr>
                            <tr>
                                <td>123456783</td>
                                <td>Fernández Reyna Mario Alberto</td>
                                <td>Instituto de Ciencias Sociales</td>
                                <td><button class="btn btn--db-index">Ver</button></td>
                            </tr>
                            <tr>
                                <td>123456784</td>
                                <td>Navarro Pérez Fernando</td>
                                <td>Facultad de Medicina y Nutrición</td>
                                <td><button class="btn btn--db-index">Ver</button></td>
                            </tr>
                            <tr>
                                <td>123456782</td>
                                <td>Rodríguez Sandoval Juan Fernando</td>
                                <td>Facultad de Medicina Veterinaria y Zootecnia</td>
                                <td><button class="btn btn--db-index">Ver</button></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="list-container">
                    <div class="record">
                        <p class="record__name"><strong>Abreu Fernández Carolina <span><img src="/static/img/Vector.png" alt="ver mas"></span></strong></p>
                        <div class="record__contaier">
                            <div class="record__container--sub title">
                                <p>Matrícula </p>
                                <p>U.A.</p>
                            </div>
                            <div class="record__container--sub subtitle">
                                <p>123456781</p>
                                <p>FADER, FECA</p>
                            </div>
                        </div>
                    </div>
                    <div class="record">
                        <p class="record__name"><strong>Abreu Fernández Carolina <span><img src="/static/img/Vector.png" alt="ver mas"></span></strong></p>
                        <div class="record__contaier">
                            <div class="record__container--sub title">
                                <p>Matrícula </p>
                                <p>U.A.</p>
                            </div>
                            <div class="record__container--sub subtitle">
                                <p>123456781</p>
                                <p>FADER, FECA</p>
                            </div>
                        </div>
                    </div>
                    <div class="record">
                        <p class="record__name"><strong>Abreu Fernández Carolina <span><img src="/static/img/Vector.png" alt="ver mas"></span></strong></p>
                        <div class="record__contaier">
                            <div class="record__container--sub title">
                                <p>Matrícula </p>
                                <p>U.A.</p>
                            </div>
                            <div class="record__container--sub subtitle">
                                <p>123456781</p>
                                <p>FADER, FECA</p>
                            </div>
                        </div>
                    </div>
                    <div class="record">
                        <p class="record__name"><strong>Abreu Fernández Carolina <span><img src="/static/img/Vector.png" alt="ver mas"></span></strong></p>
                        <div class="record__contaier">
                            <div class="record__container--sub title">
                                <p>Matrícula </p>
                                <p>U.A.</p>
                            </div>
                            <div class="record__container--sub subtitle">
                                <p>123456781</p>
                                <p>FADER, FECA</p>
                            </div>
                        </div>
                    </div>
                </div>
                
                <nav role="navegation" class="pagination-container">
                    <ul class="pagination pagination--dashboard">
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
                            <button class="pagination-item">4</button>
                        </li>
                        <li>
                            <button class="pagination-item">...</button>
                        </li>
                        <li>
                            <button class="pagination-item">20</button>
                        </li>
                        <li>
                            <button class="pagination-next">
                                <span class="pagination-next__icon"><span class="pagination-next__text">Siguiente</span><img src="/static/img/Vector.png" alt="icon next"></span>
                            </button>
                        </li>
                    </ul>
                    <div class="pagination--responsive">
                        <button class="pagination-previous pagination-previous--disabled"><span class="pagination-previous__icon mr-1"><img src="/static/img/icon-prev.png" alt="prev"></span></button>
                        <div class="pagination-pages">
                            <select name="pagination" id="pagination" class="form-field-p">
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">14</option>
                            </select>
                            <span>de 14</span>
                        </div>
                        <button type="button" rel="next" class="pagination-next"><span class="pagination-next__icon"><img src="/static/img/icon-next.png" alt="next"></span></button>
                    </div>
                </nav>
            </div>
        </div>
    </section>
</template>
<script>
    export default {
		name: 'profesores',
    }
</script>