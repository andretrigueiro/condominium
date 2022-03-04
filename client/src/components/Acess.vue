<template>
  <div class="acess">

    <div class="login-button">
      <b-button type="button" size="lg" variant="success" v-b-modal.login-modal>
        Login
      </b-button>

      <!-- LOG IN MODAL -->
      <b-modal ref="LogInModal"
              id="login-modal"
              title="Login"
              hide-footer>
        <b-form @submit="onSubmitLogin" class="w-100">
          <b-form-group id="form-user-group"
                      label="User:"
                      label-for="form-user-input">
            <b-form-input id="form-user-input"
                          type="text"
                          v-model="loginUserForm.user"
                          required
                          placeholder="Enter User">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-password-group"
                        label="Password:"
                        label-for="form-password-input">
            <b-form-input id="form-password-input"
                          type="text"
                          v-model="loginUserForm.password"
                          required
                          placeholder="Enter Password">
            </b-form-input>
          </b-form-group>
          <b-button-group>
            <b-button type="submit" variant="primary">Submit</b-button>
          </b-button-group>
        </b-form>
        <b-alert :show="showMessage" dismissible>
          {{ message }}
        </b-alert>
      </b-modal>
    </div>

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Acess',
  data() {
    return {
      user_id_logged: '',
      type: '',
      message: '',
      showMessage: false,
      loginUserForm: {
        user: '',
        password: '',
      },
    };
  },
  computed: {
    user_logged() {
      return this.user_id_logged;
    },
  },
  methods: {
    loginUser(payload) {
      const path = 'http://localhost:5000/auth/login';
      axios.post(path, payload)
        .then((res) => {
          if (res.data.message === 'User logged in!' && res.data.user !== '') {
            this.message = res.data.message;
            this.user_id_logged = res.data.user;
            this.type = res.data.type;
            this.$cookies.set('user', this.user_id_logged);
            this.$refs.LogInModal.hide();
            if (this.type === 'resident') {
              this.$router.push('Resident');
            } else if (this.type === 'adm') {
              this.$router.push('Adm');
            }
          } else {
            this.showMessage = true;
            this.message = res.data.message;
          }
          console.log(this.user_id_logged);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onSubmitLogin(evt) {
      evt.preventDefault();
      const payload = {
        user: this.loginUserForm.user,
        password: this.loginUserForm.password,
      };
      this.loginUser(payload);
      this.initForm();
    },
    initForm() {
      this.loginUserForm.user = '';
      this.loginUserForm.password = '';
    },
  },
};
</script>

<style scoped>

.login-button{
  margin-top: 30px;
}

</style>
