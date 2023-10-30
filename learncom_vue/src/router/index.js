import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import SignUpView from '../views/SignUpView.vue'
import LoginView from '../views/LoginView.vue'
import MyAccountView from '../views/dashboard/MyAccountView.vue'
import CoursesView from '../views/CoursesView.vue'
import CourseDeatail from '../views/CourseDetail.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },

  {
    path: '/dashboard/my-account',
    name: 'myaccount',
    component: MyAccountView
  },

  {
    path: '/courses',
    name: 'courses',
    component: CoursesView
  },

  {
    path: '/courses/:slug',
    name: 'course-detail',
    component: CourseDeatail,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
