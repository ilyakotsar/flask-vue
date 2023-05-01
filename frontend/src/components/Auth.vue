<script>
export default {
  props: {
    mode: String,
  },
  data() {
    return {
        title: ''
    }
  },
  mounted() {
    if (this.mode == 'sign-up') {
        this.title = 'Sign Up';
    }
    else {
        this.title = 'Sign In';
    }
  }
}
</script>

<template>
  <div class="container mt-4">
    <h5 class="text-center pb-2">{{ title }}</h5>
    <div class="card p-3">
      <div class="form-floating mb-3">
        <input type="email" class="form-control" id="email" placeholder="">
        <label for="email">Email</label>
      </div>
      <div class="form-floating mb-3">
        <input type="password" class="form-control" id="password" placeholder="">
        <label for="password">Password</label>
      </div>
      <button type="button" class="btn btn-primary" disabled>{{ title }}</button>
    </div>
  </div>
</template>

<style scoped>
.container {
  max-width: 350px;
}
</style>