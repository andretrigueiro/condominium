<template>
  <div id="main-header">
    <b-navbar toggleable="lg" sticky id="nav-header">
      <b-navbar-brand class="text-modifier" to="/">CONDOMINIUM</b-navbar-brand>
    </b-navbar>
  </div>
</template>

<script>

export default {
  name: 'Header',
  data() {
    return {
      user_logged: '',
      message: '',
      showMessage: true,
    };
  },
};
</script>

<style scoped>

#main-header {
  background-color: white;
  padding-bottom: 5px;
  padding-top: 10px;
  border-bottom: dimgrey;
  border-bottom-width: 1px;
  border-bottom-style: solid;
}

#nav-header {
  margin-left: 5%;
  margin-right: 5%;
  font-size: 18px !important;
  font-weight: 600 !important;
}

.text-modifier{
  color: red !important;
}

.nav-link{
  color: red !important;
}

.space{
  margin-left: 10px;
  margin-right: 10px;
}

</style>
