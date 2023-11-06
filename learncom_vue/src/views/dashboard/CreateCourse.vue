<template>
    <div class="about">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">Create Course</h1>
            </div>
        </div>

        <section class="section">

            <div class="px-6 py-4 has-background-grey-lighter">
                <h2 class="subtitle">Meta infomation</h2>

                <div class="field">
                    <label>Title</label>
                    <input type="text" class="input" v-model="form.title">
                </div>

                <div class="field">
                    <label>Short description</label>
                    <textarea type="text" class="input" v-model="form.short_desription" />
                </div>

                <div class="field">
                    <label>Long description</label>
                    <textarea type="text" class="input" v-model="form.long_desription" />
                </div>

                <div class="field">
                    <div class="select is-multiple">
                        <select multiple size="10" v-model="form.categories">
                            <option v-for="category in categories" v-bind="category.id" v-bind:value="category.id">
                                {{ category.title }}
                            </option>

                        </select>
                    </div>
                </div>
            </div>

            <div class="mt-6 px-6 py-4 has-background-grey-lighter">
                <h2 class="subtitle">Lessons infomation</h2>
                <hr>

                <div v-for="(lesson, index) in form.lessons" v-bind:key="index" class="mb-4">

                    <h3 class="subtitle is-size-6">Lesson</h3>
                    <div class="field">
                        <label>Title</label>
                        <input type="text" class="input" v-model="lesson.title" :name="`form.lessons[${index}][title]`">
                    </div>
                    <div class="field">
                        <label>Short description</label>
                        <textarea type="text" class="input" v-model="lesson.short_desription" :name="`form.lessons[${index}][short_desription]`"/>
                    </div>

                    <div class="field">
                        <label>Long description</label>
                        <textarea type="text" class="input" v-model="lesson.long_desription" :name="`form.lessons[${index}][long_desription]`"/>
                    </div>

                </div>
                <button class="button is-primary" @click="addLesson()">Add lesson</button>
            </div>


            <div class="field buttons">
                <button class="button is-success" @click="submitForm('draft')">Save as draft</button>
                <button class="button is-info" @click="submitForm('review')">Submit for review</button>
            </div>

        </section>

    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            form: {
                title: '',
                short_desription: '',
                long_desription: '',
                categories: [],
                status: '',
                lessons: [],
            },
            categories: [],

        }
    },

    mounted() {
        this.getCategories()
    },

    methods: {
        getCategories() {
            axios
                .get('courses/get-categories/')
                .then(response => {
                    this.categories = response.data

                })
        },

        submitForm(status) {

            this.form.status = status
            console.log(this.form)
            axios
                .post('courses/create/', this.form)
                .then(response => {
                    console.log(response.data)
                })
                .catch(error => {
                    console.log('error:', error)
                })
        },

        addLesson() {
            console.log("Lesson work")

            this.form.lessons.push({
                title: '',
                short_desription: '',
                long_desription: ''
            })
        }
    }

}
</script>