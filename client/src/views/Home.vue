<template>
  <div class="homepage">
    <b-jumbotron header="Condominium" lead="Welcome to the Condominium homepage">
      <p>Log in to start</p>
      <Acess/>
    </b-jumbotron>
  </div>
</template>

<script>
import Acess from '../components/Acess.vue';

export default {
  name: 'Home',
  data() {
    return {
      message: '',
    };
  },
  components: {
    Acess,
  },
};

</script>
