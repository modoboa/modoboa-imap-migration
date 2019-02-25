import Vue from 'vue'
import Router from 'vue-router'
import Providers from './views/Providers.vue'

Vue.use(Router)

export default new Router({
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'providers',
            component: Providers
        }
    ]
})
