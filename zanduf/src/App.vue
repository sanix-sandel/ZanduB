<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to ZanduB"/>

    <div class="page-wrapper chiller-theme toggled">
   <a id="show-sidebar" class="btn btn-sm btn-dark" href="#">
     <i class="fas fa-bars"></i>
   </a>
   <nav id="sidebar" class="sidebar-wrapper">
     <div class="sidebar-content">
       <div class="sidebar-brand">
         <a href="#"><p>ZanduB</p></a>
         <div id="close-sidebar">
           <i class="fas fa-times"></i>
         </div>
       </div>
       
        <div class="sidebar-header">
          <!--<div class="user-pic">
              <img class="img-responsive center-block" src="https://raw.githubusercontent.com/azouaoui-med/pro-sidebar-template/gh-pages/src/img/user.jpg"
              alt="User picture">
            </div>-->
          <div class="avatar">
            <img alt="" src="">
          </div>
            <div class="user-info">
              <a href="#"><span class="user-name">
                <strong>Username</strong></span></a>
              <span class="user-role">Administrator</span>
              <span class="user-status">
                <i class="fa fa-circle"></i>
                <span>Online</span>
              </span>
            </div>
        </div>
       
      <!-- sidebar-header  -->
      <div class="sidebar-search">
        <div>
          <div class="input-group">
            <form action="{% url 'searching:search' %}">
              <input name="q" type="text" class="form-control search-menu" placeholder="Search...">
              <div class="input-group-append">
                <span class="input-group-text">
                  <i class="fa fa-search" aria-hidden="true"></i>
                </span>
              </div>
            </form>
            
          </div>
        </div>
      </div>
      <!-- sidebar-search  -->
      <div class="sidebar-menu">
        <ul>
          <li class="header-menu">
            <span>Menu</span>
          </li>
          <li class="sidebar-dropdown">
            <a href="#">
              <i class="fa fa-tachometer-alt"></i>
              <span>Acceuil</span>
              <span class="badge badge-pill badge-warning">New</span>
            </a>
            <div class="sidebar-submenu">
              <ul>
                <li>
                  <a href="#">Vendre
                    <span class="badge badge-pill badge-success">Pro</span>
                  </a>
                </li>
                <li>
                  <a href="#">Dashboard 2</a>
                </li>
                <li>
                  <a href="#">Dashboard 3</a>
                </li>
              </ul>
            </div>
          </li>
          <li class="sidebar-dropdown">
            <a href="#">
              <i class="fa fa-shopping-cart"></i>
              <span>Stores</span>
              <span class="badge badge-pill badge-danger">3</span>
            </a>
            <div class="sidebar-submenu">
              <ul>
                <li>
                  
                  <a href="#">My Store
            
                  </a>
                </li>
                <li>
                  <a href="#">Mes stores favoris</a>
                </li>
                <li>
                  <a href="#">Tous les stores</a>
                </li>
                <li>
                  <a href="#">Annonces</a>
                </li>
                <li>
                  <a href="#">Mes Achats</a>
                </li>
                <li>
                  <a href="#">Mes ventes</a>
                </li>
              </ul>
            </div>
          </li>
          <li class="sidebar-dropdown">
            <a href="#">
              <i class="fa fa-list"></i>
              <span>Categories</span>
            </a>
            <div class="sidebar-submenu">
              <ul>
                category
              </ul>
            </div>
          </li>
          <li class="sidebar-dropdown">
            <a href="#">
              <i class="fa fa-heart"></i>
              <span>Articles aimes</span>
            </a>
            
          </li>
          <li class="sidebar-dropdown">
            <a href="#">
              <i class="fa fa-chart-line"></i>
              <span>Groupes</span>
            </a>
            <div class="sidebar-submenu">
              <ul>
                <li>
                  <a href="#">Pie chart</a>
                </li>
                <li>
                  <a href="#">Line chart</a>
                </li>
                <li>
                  <a href="#">Bar chart</a>
                </li>
                <li>
                  <a href="#">Histogram</a>
                </li>
              </ul>
            </div>
          </li>
          <li class="sidebar-dropdown">
            <a href="#">
              <i class="fa fa-globe"></i>
              <span>Maps/Carte</span>
            </a>
            <div class="sidebar-submenu">
              <ul>
                <li>
                  <a href="#">Google maps</a>
                </li>
                <li>
                  <a href="#">Open street map</a>
                </li>
              </ul>
            </div>
          </li>
          <li class="header-menu">
            <span>Extra</span>
          </li>
          <li>
            <a href="#">
              <i class="fa fa-book"></i>
              <span>Documentation</span>
              <span class="badge badge-pill badge-primary">Beta</span>
            </a>
          </li>
          <li>
            <a href="#">
              <i class="fa fa-calendar"></i>
              <span>Calendar</span>
            </a>
          </li>
          <li>
            <a href="#">
              <i class="fa fa-folder"></i>
              <span>Examples</span>
            </a>
          </li>
        </ul>
      </div>
      <!-- sidebar-menu  -->
    </div>
    <!-- sidebar-content  -->
    <div class="sidebar-footer">
      <a href="#">
        <i class="fa fa-bell"></i>
        <span class="badge badge-pill badge-warning notification">
          n
        </span>
      </a>
      <a href="#">
        <i class="fa fa-envelope"></i>
        <span class="badge badge-pill badge-success notification">7</span>
      </a>
      <a href="#">
        <i class="fa fa-cog"></i>
        <span class="badge-sonar"></span>
      </a>
      
      <a href="#">
        <i class="fa fa-power-off"></i>
      </a>
      
      
        
    </div>

  </nav>
  <!-- sidebar-wrapper  -->

  <header>
    <!-- Fixed navbar -->
    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4\
     mb-3 bg-white border-bottom shadow-sm">
      <a href="#" class="navbar-brand my-0 mr-md-auto font-weight-normal">ZanduB</a>
      <nav class="my-2 my-md-0 mr-md-3">
        <a class="p-2 text-dark" href="#"> Tous les Products</a>
      
        <a class="p-2 text-dark" href="#">About</a>
        
          <!--<a class="p-2 text-dark" href="{% url 'account_logout' %}">Se Deconne</a>-->
        
         <!----> <a class="btn btn-outline-primary" href="#">Se Connecter</a>
        <a class="btn btn-outline-primary"
            href="#">S'Enregistrer</a>
      
      </nav>
    </div>

    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4\
     mb-3 bg-white border-bottom shadow-sm">
      <p>for tags trending tags</p>
      
    </div>
  </header>


  <main class="page-content">
    <!--
    {% block content %}
    {% endblock %}
-->
      <footer class="text-center">
        <div class="mb-2">
          <small>
            © 2020 made with <i class="fa fa-heart" style="color:red"></i> by - <a target="_blank" rel="noopener noreferrer" href="https://azouaoui.netlify.com">
              Mohamed Azouaoui
            </a>
          </small>
        </div>
        <div>
          <a href="https://github.com/azouaoui-med" target="_blank">
            <img alt="GitHub followers" src="https://img.shields.io/github/followers/azouaoui-med?label=github&style=social" />
          </a>
          <a href="https://twitter.com/azouaoui_med" target="_blank">
            <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/azouaoui_med?label=twitter&style=social" />
          </a>
        </div>
    </footer>

  </main>
   <!-- page-content" -->

 </div>
<!-- page-wrapper -->
  


  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;



  


}
</style>
