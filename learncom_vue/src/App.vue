<template>
  <div>
    <NavigationComponent />
    <router-view />
    <FooterComponent />
  </div>
</template>


<script>
import NavigationComponent from '@/components/NavigationComponent.vue'
import FooterComponent from '@/components/FooterComponent.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    NavigationComponent,
    FooterComponent,
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.user.token

    if (token){
      axios.defaults.headers.common['Authorization'] = "Token " + token
    }else{
      axios.defaults.headers.common['Authorization'] = ""
    }
  }
}
</script>
<style lang="scss">
@import '~bulma/css/bulma.css';
</style>
