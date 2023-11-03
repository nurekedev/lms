<template>
    <div class="courses">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title"> {{ created_by.first_name + ' ' + created_by.last_name}} </h1>
            </div>
        </div>

        <section class="section">
            <div class="container">

                <div class="columns is-multiline">

                    <div class="column is-4" v-for="course in courses" v-bind:key="course.id">

                        <CourseItemComponent :course="course" />
                    </div>

                    <div class="column is-12">
                        <div class="pagination">
                            <a class="pagination-previous">Previous</a>
                            <a class="pagination-next">Next</a>
                            <ul class="pagination-list">
                                <li>
                                    <a class="pagination-link is-current">1</a>
                                </li>
                            </ul>
                        </div>
                    </div>

                </div>
            </div>

        </section>
    </div>
</template>

<script>
import CourseItemComponent from '@/components/CourseItemComponent.vue';
import router from '@/router';
import axios from 'axios';
export default {
    data() {
        return {
            courses: [],
            created_by: {}

        };
    },
    async mounted() {
        console.log("Mounted");

        this.getCourses()

    },
    components: { router, CourseItemComponent },
    methods: {

        getCourses() {
            
            axios
                .get(`courses/get-author-course/${this.$route.params.id}/`)
                .then(response => {
                    console.log(response.data);
                    console.log('Axios works');
                    this.courses = response.data.courses;
                    this.created_by = response.data.created_by
                });
            

        }
    }
}
</script>