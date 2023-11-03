<template>
    <nav class="navbar" role="navigation" aria-label="main navigation" style="min-height: 5rem;">
        <div class="navbar-brand">
            <router-link class="navbar-item is-size-4" to="/">LMS</router-link>
        </div>

        <!-- Navbar elements-->
        <div id="navbar-item" class="navbar-menu">

            <div class="navbar-start">
                <router-link to="/" class="navbar-item">Home</router-link>
                <router-link to="/about" class="navbar-item">About</router-link>
                <router-link to="/courses" class="navbar-item">Courses</router-link>
            </div>

            <div class="navbar-end">
                <div class="navbar-item">
                    <div class="buttons">
                        <template v-if="this.$store.state.user.isAuthenticated">
                            <router-link to="/dashboard/create_course/" class="button is-primary">
                                Create Course
                            </router-link>
                            <router-link to="/dashboard/my-account/" class="button is-info">
                                My account
                            </router-link>
                        </template>

                        <template v-else>
                            <router-link to="/signup" class="button is-primary"><strong>Sign up</strong></router-link>
                            <router-link to='/login' class="button is-light">Log in</router-link>
                        </template>
                    </div>
                </div>
            </div>

        </div>

    </nav>
</template>