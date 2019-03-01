import Vue from 'vue'
import Router from 'vue-router'
import Providers from './views/Providers.vue'
import Migrations from './views/Migrations.vue'

Vue.use(Router)

export default new Router({
    base: process.env.BASE_URL,
    linkActiveClass: 'active',
    routes: [
        {
            path: '/',
            name: 'providers',
            component: Providers
        },
        {
            path: '/migrations',
            name: 'migrations',
            component: Migrations
        }
    ]
})
