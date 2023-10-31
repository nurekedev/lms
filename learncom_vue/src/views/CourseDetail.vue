<template>
    <div class="courses">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title"> {{ course.title }} </h1>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns content">
                    <div class="column is-2">
                        <h2>Table of contents</h2>
                        <ul>
                            <li v-for="lesson in lessons" v-bind:key="lesson.id">
                                <a @click="activeLesson = lesson">{{ lesson.title }}</a>
                            </li>
                        </ul>
                    </div>

                    <div class="column is-10">
                        <h2>Introduction</h2>
                        <template v-if="$store.state.user.isAuthenticated">
                            <template v-if="activeLesson">
                                <h2>{{ activeLesson.title }}</h2>
                                {{ activeLesson.long_desription }}
                            </template>

                            <template v-else>
                                <p>{{ course.long_desription }}</p>
                            </template>

                        </template>
                        <template v-else>
                            <h2> Restricted access </h2>
                            <p>Please sig in</p>
                        </template>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>
<script>
import router from '@/router';
import axios from 'axios';
export default {
    data() {
        return {
            course: {},
            lessons: [],
            activeLesson: null,
        };
    },
    mounted() {

        const slug = this.$route.params.slug
        axios
            .get(`/api/v1/courses/${slug}/`)
            .then(response => {
                console.log(response.data);
                this.course = response.data.course;
                this.lessons = response.data.lessons;
            });
    },
    components: { router }
}
</script>