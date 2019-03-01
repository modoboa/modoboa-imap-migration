<template>
<div id="app">
  <div id="leftcol" class="sidebar collapse navbar-collapse">
    <ul class="nav nav-sidebar" role="menu">
      <router-link tag="li" :to="{ name: 'providers' }" exact>
        <a><translate>Email providers</translate></a>
      </router-link>
      <router-link tag="li" :to="{ name: 'migrations' }" exact>
        <a><translate>Migrations</translate></a>
      </router-link>
    </ul>
  </div>
  <div class="main">
    <router-view/>
  </div>
</div>
</template>
