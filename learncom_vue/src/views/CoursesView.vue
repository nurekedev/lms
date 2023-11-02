<template>
    <div class="courses">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title"> Courses </h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns">

                    <div class="column is-2">
                        <aside class="menu">
                            <p class="menu-label">
                                Categories
                            </p>
                            <ul class="menu-list">
                                <li>
                                    <a v-bind:class="{'is-active': !activeCategory }" @click="setActiveCategory(null)">
                                        All courses</a>

                                </li>
                                <li v-for="category in categories" v-bind:key="category.id"
                                    @click="setActiveCategory(category)">

                                    <a>{{ category.title }}</a>
                                </li>

                            </ul>
                        </aside>
                    </div>

                    <div class="column is-10">
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
            categories: [],
            activeCategory: null
        };
    },
    async mounted() {
        console.log("Mounted");

        document.title = 'Courses | LMS'
        await axios
            .get('courses/get-categories/')
            .then(response => {
                console.log(response.data)
                this.categories = response.data
            })

        this.getCourses()

    },
    components: { router, CourseItemComponent },
    methods: {
        setActiveCategory(category) {
            this.activeCategory = category
            this.getCourses()
        },

        getCourses() {
            let url = 'courses/'
            if (this.activeCategory) {
                url += '?category_id=' + this.activeCategory.id
            }
            axios
                .get(url)
                .then(response => {
                    console.log(response.data);
                    this.courses = response.data;
                });

        }
    }
}
</script>