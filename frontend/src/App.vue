<template>
<div id="app">
  <div id="leftcol" class="sidebar collapse navbar-collapse">
    <ul class="nav nav-sidebar" role="menu">
      <li><router-link :to="{ name: 'providers' }">
          <translate>Email providers</translate></router-link></li>
    </ul>
  </div>
  <div class="main">
    <router-view/>
  </div>
</div>
</template>
