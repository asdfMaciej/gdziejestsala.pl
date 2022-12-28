import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SelectStartView from '../views/SelectStartView.vue'
import SelectDestinationView from '../views/SelectDestinationView.vue'
import RouteView from '../views/RouteView.vue'
import PointView from '../views/PointView.vue'
import AboutView from '../views/AboutView.vue'
import FloorView from '../views/FloorView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/route/',
      name: 'select-start',
      component: SelectStartView
    },
    {
      path: '/route/:start_id/',
      name: 'select-destination',
      component: SelectDestinationView
    },
    {
      path: '/route/:start_id/:destination_id/',
      name: 'view-route',
      component: RouteView
    },
    {
      path: '/point/:point_id/',
      name: 'view-point',
      component: PointView
    },
    {
      path: '/floor/:floor_id/',
      name: 'view-floor',
      component: FloorView
    },
    {
      path: '/about/',
      name: 'about',
      component: AboutView
    },
  ]
})

export default router
