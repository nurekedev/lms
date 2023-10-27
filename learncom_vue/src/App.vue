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
export default {
  name: 'App',
  components: {
    NavigationComponent,
    FooterComponent,
  }
}
</script>
<style lang="scss">
@import '~bulma/css/bulma.css';
</style>
