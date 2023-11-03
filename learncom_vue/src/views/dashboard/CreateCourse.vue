<template>
    <div class="about">
        <div class="hero is-info">
            <div class="hero-body has-text-centered">
                <h1 class="title">Create Course</h1>
            </div>
        </div>

        <section class="section">

            <form v-on:submit.prevent="submitForm">

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
                            <option
                            v-for="category in categories"
                            v-bind="category.id"
                            v-bind:value="category.id" 
                            >
                            {{ category.title }}
                            </option>

                        </select>
                    </div>
                </div>

                <div class="field">
                    <button class="is-success">Submit</button>
                </div>
            </form>
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

        submitForm(){
            axios
                .post('courses/create/', this.form)
                .then(response=>{
                    console.log(response.data)
                })
                .catch(error=>{
                    console.log('error:', error)
                })
        }
    }

}
</script>