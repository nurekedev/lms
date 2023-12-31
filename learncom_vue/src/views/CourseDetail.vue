<template>
    <div class="courses">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title"> {{ course.title }} </h1>
                <router-link
                :to="{name: 'author', params:{id: course.created_by.id}}"
                class="subtitle">by {{ course.created_by.first_name + ' ' + course.created_by.last_name}}</router-link>
            </div>
        </div>

        <section class="section">
            <div class="container">
                <div class="columns content">
                    <div class="column is-2">
                        <h2>Table of contents</h2>
                        <ul>
                            <li v-for="lesson in lessons" v-bind:key="lesson.id">
                                <a @click="setActiveLesson(lesson)">{{ lesson.title }}</a>
                            </li>
                        </ul>
                    </div>

                    <div class="column is-10">
                        <h2>Introduction</h2>
                        <template v-if="$store.state.user.isAuthenticated">
                            <template v-if="activeLesson">
                                <h2>{{ activeLesson.title }}</h2>
                                <hr>

                                <span class="tag is-warning" v-if="activity.status == 'started'" @click="markAsDone">
                                    Started
                                </span>

                                <span class="tag is-success" v-else="activity.status == 'done'">
                                    Done
                                </span>

                                <hr>
                                {{ activeLesson.long_desription }}
                                <hr>

                                <template v-if="activeLesson.lesson_type === 'quiz'">
                                    <QuizComponent v-bind:quiz="quiz" />
                                </template>

                                <template v-if="activeLesson.lesson_type === 'video'">
                                    <VideoComponent v-bind:youtube_id="activeLesson.youtube_id" />
                                </template>

                                <template v-if="activeLesson.lesson_type === 'article'">
                                    <CommentComponent v-for="comment in comments" v-bind:key="comment.id"
                                        v-bind:comment="comment" />

                                    <AddCommentComponent v-bind:course="course" v-bind:active-lesson="activeLesson"
                                        v-on:submitComment="submitComment" />

                                </template>
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
import CommentComponent from '@/components/CommentComponent.vue';
import AddCommentComponent from '@/components/AddCommentComponent.vue';
import QuizComponent from '@/components/QuizComponent.vue';
import VideoComponent from '@/components/VideoComponent.vue';


export default {
    data() {
        return {
            course: {
                created_by: {
                    id: 0
                }
            },
            lessons: [],
            activeLesson: null,
            errors: [],
            comments: [],
            quiz: {},
            selectedAnswer: '',
            quizResult: null,
            activity: {},

        };
    },
    async mounted() {

        const slug = this.$route.params.slug
        await axios
            .get(`/courses/${slug}/`)
            .then(response => {
                console.log(response.data);
                this.course = response.data.course;
                this.lessons = response.data.lessons;
            });

        document.title = this.course.title
    },

    methods: {

        submitComment(comment) {
            this.comments.push(comment)
        },

        setActiveLesson(lesson) {
            this.activeLesson = lesson

            if (lesson.lesson_type === 'quiz') {
                this.getQuiz()
            } else {
                this.getComments()
            }

            this.trackStarted()
        },

        trackStarted() {
            axios
                .post(`activities/track-started/${this.$route.params.slug}/${this.activeLesson.slug}/`)
                .then(response => {
                    console.log(response.data)
                    this.activity = response.data

                })
                .catch(error => {
                    console.log(error.data)
                })

        },

        markAsDone() {
            axios
                .post(`activities/mark-as-done/${this.$route.params.slug}/${this.activeLesson.slug}/`)
                .then(response => {
                    console.log(response.data)
                    this.activity = response.data

                })
                .catch(error => {
                    console.log(error.data)
                })

        },

        getQuiz() {
            axios
                .get(`courses/${this.course.slug}/${this.activeLesson.slug}/get-quiz/`)
                .then(response => {
                    this.quiz = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        getComments() {

            axios
                .get(`courses/${this.course.slug}/${this.activeLesson.slug}/get-comments`)
                .then(response => {
                    console.log(response.data)
                    this.comments = response.data
                })

        }
    },


    components: { router, CommentComponent, AddCommentComponent, QuizComponent, VideoComponent }
}
</script>