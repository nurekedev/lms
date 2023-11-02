<template>
  <div class="home">

    <div class="hero is-info is-medium">
      <div class="hero-body has-text-centered">
        <h1 class="title"> Welcome to LMS</h1>
        <h3 class="subtitle"> Learning is action of future</h3>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns is-multiline">
          <div class="column is-4">
            <div class="box has-text-centered">

              <span class="icon is-size-2 hast-text-info">
                <i class="far fa-clock"></i>
              </span>

              <h2 class="is-size-4 mt-4 mb-4">Study on own place</h2>
              <p>random text</p>

            </div>

          </div>

          <div class="column is-4">
            <div class="box has-text-centered">

              <span class="icon is-size-2 hast-text-info">
                <i class="far fa-comments"></i>
              </span>

              <h2 class="is-size-4 mt-4 mb-4">Study with others</h2>
              <p>random text</p>

            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">

              <span class="icon is-size-2 hast-text-info">
                <i class="far fa-home"></i>
              </span>

              <h2 class="is-size-4 mt-4 mb-4">Study from your home</h2>
              <p>random text</p>

            </div>
          </div>

          <div class="column is-12 has-text-centered">
            <a href="/signup" class="button is-info is-size-3 mt-6 mb-6">Get started</a>
          </div>

          <hr>

          <div class="column is-3" v-for="course in courses" v-bind:key="course.id">
            <CourseItemComponent :course="course" />
          </div>

        </div>
      </div>
    </section>

  </div>
</template>

<script>
import CourseItemComponent from '@/components/CourseItemComponent.vue'
import axios from 'axios'

export default {
  name: 'HomeView',

  data() {
    return {
      courses: []
    }
  },

  components: {
    CourseItemComponent
  },

  mounted() {

    document.title = 'Welcome | LMS'
    axios
      .get('/courses/get-newest-courses/')
      .then(response => {
        this.courses = response.data
      })
  }


}
</script>
