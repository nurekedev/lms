<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-4by3">
                <img :src="course.get_image">
            </figure>
        </div>

        <div class="card-content">
            <div class="media">
                <div class="media-content">
                    <p class="is-size-5">{{ course.title }}</p>
                </div>
            </div>

            <div class="content">
                <p>{{ course.short_desription }}</p>


                <router-link :to="{ name: 'course-detail', params: { slug: course.slug } }">view
                    more</router-link>
            </div>
        </div>

    </div>
</template>

<script>

export default {
    props: ['course']
}
</script>