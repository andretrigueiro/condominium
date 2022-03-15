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

      <!-- FIRST LOGIN MODAL -->
      <b-modal ref="FirstLoginModal"
              id="first-login-modal"
              title="First Login"
              hide-footer>
        <b-form @submit="onSubmitFirstLogin" class="w-100">
          <p>This is your first login!!!</p>
          <p>Change your password, its your birthdate.</p>
          <b-form-group id="form-user-group"
                      label="User:"
                      label-for="form-user-input">
            <b-form-input id="form-user-input"
                          type="text"
                          v-model="firstLoginUserForm.user"
                          required
                          placeholder="Enter User">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-password-group"
                        label="Password:"
                        label-for="form-new-password-input">
            <b-form-input id="form-new-password-input"
                          type="text"
                          v-model="firstLoginUserForm.password"
                          required
                          placeholder="Enter New Password">
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
      first_login: '',
      type: '',
      house_number: '',
      message: '',
      showMessage: false,
      loginUserForm: {
        user: '',
        password: '',
      },
      firstLoginUserForm: {
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
      const path = 'http://18.231.124.87:7011/auth/login';
      axios.post(path, payload)
        .then((res) => {
          if (res.data.message === 'User logged in!' && res.data.user !== '') {
            this.message = res.data.message;
            this.user_id_logged = res.data.user;
            this.first_login = res.data.first_login;
            this.type = res.data.type;
            this.house_number = res.data.house_number;
            this.$cookies.set('user', this.user_id_logged);
            this.$cookies.set('house', this.house_number);
            this.$refs.LogInModal.hide();

            if (this.first_login === 'true') {
              this.$refs.FirstLoginModal.show();
            }

            if (this.type === 'resident') {
              this.$router.push('Resident');
            } else if (this.type === 'adm') {
              this.$router.push('Adm');
            }
          } else {
            this.showMessage = true;
            this.message = res.data.message;
          }
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
    firstLoginUser(payload) {
      const path = 'http://18.231.124.87:7011/auth/change_password';
      axios.post(path, payload)
        .then((res) => {
          if (res.data.message === 'Password changed!') {
            this.$refs.FirstLoginModal.hide();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onSubmitFirstLogin(evt) {
      evt.preventDefault();
      const payload = {
        user: this.firstLoginUserForm.user,
        password: this.firstLoginUserForm.password,
      };
      this.firstLoginUser(payload);
      this.initForm();
    },
    initForm() {
      this.loginUserForm.user = '';
      this.loginUserForm.password = '';
      this.firstLoginUserForm.user = '';
      this.firstLoginUserForm.password = '';
    },
  },
};
</script>

<style scoped>

.login-button{
  margin-top: 30px;
}

</style>
