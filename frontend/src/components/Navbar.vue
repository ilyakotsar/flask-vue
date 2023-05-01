<script>
import { RouterLink } from 'vue-router';
import Cookies from 'js-cookie';

export default {
  props: {
    active: String,
  },
  data() {
    return {
      theme: '',
    }
  },
  mounted() {
    const themeCookie = Cookies.get('theme');
    if (themeCookie === undefined) {
      this.theme = 'light';
    }
    else {
      this.theme = themeCookie;
    }
    document.body.className = `${this.theme}-theme`;
    if (this.active !== 'home') {
      document.getElementById(this.active).classList.add('active-link');
    }
  },
  methods: {
    toggleTheme() {
      if (this.theme === 'light') {
        this.theme = 'dark';
      }
      else {
        this.theme = 'light';
      }
      document.body.className = `${this.theme}-theme`;
      Cookies.set('theme', this.theme, {sameSite: 'strict'});
    }
  }
}
</script>

<template>
  <nav>
    <div class="container-fluid d-flex justify-content-between align-items-center pe-1">
      <RouterLink to="/">
        <img src="/favicon.ico" alt="Logo" width="23">
      </RouterLink>
      <div class="d-flex flex-row ms-auto align-items-center">
        <RouterLink to="sign-in" id="sign-in" class="link-nav">Sign In</RouterLink>
        <RouterLink to="sign-up" id="sign-up" class="link-nav">Sign Up</RouterLink>
        <button @click="toggleTheme" class="btn btn-theme">
          <i v-if="theme == 'light'" class="bi bi-sun-fill"></i>
          <i v-else class="bi bi-moon-stars-fill"></i>
        </button>
      </div>
    </div>
  </nav>
</template>