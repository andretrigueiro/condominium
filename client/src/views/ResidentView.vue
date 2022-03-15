<template>
  <b-container fluid class="adm-interface">
    <b-row>

      <!-- MENU PART OF PAGE -->
      <b-col class="adm-sidebar" cols="2">
        <div class="menu-welcome"> Welcome, {{user_logged_in}}! </div>
        <div id="adm-menu">
          <b-list-group class="menu-part-one">

            <b-list-group-item button type="button" v-b-modal.payment-history-modal>
              Show payment history
            </b-list-group-item>
            <b-list-group-item button type="button" v-b-modal.make-payments-modal>
              Make payments
            </b-list-group-item>
            <b-list-group-item button type="button" v-b-modal.new-resident-modal>
              Register new resident
            </b-list-group-item>

          </b-list-group>
          <b-list-group class="menu-part-two">
            <b-list-group-item button>Logout</b-list-group-item>
          </b-list-group>
        </div>
      </b-col>

      <!-- SHOW PAYMENT HISTORY -->
      <b-modal ref="paymentHistoryModal"
              id="payment-history-modal"
              title="Payment History"
              hide-footer>
        <b-table striped stacked hover responsive :items="houseInfo.payments"></b-table>
      </b-modal>

      <!-- MAKE PAYMENTS -->
      <b-modal ref="makePaymentsModal"
              id="make-payments-modal"
              title="Make Payments"
              hide-footer>
        <b-table striped hover responsive :items="houseInfo.fines"></b-table>
        <p>Choose the Fine to be paid</p>

        <b-form @submit="onSubmitPayment" class="w-100">

          <b-form-select v-model="fineSelected" :options="fineOptions"></b-form-select>

          <b-button-group>
            <b-button type="submit" class="button-adjust" variant="success">Pay</b-button>
          </b-button-group>

        </b-form>
      </b-modal>

      <!-- NEW RESIDENT MODAL -->
      <b-modal ref="NewResidentModal"
              id="new-resident-modal"
              title="New Resident"
              hide-footer>
        <b-form @submit="onSubmitNewResident" class="w-100">
          <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
            <b-form-input id="form-name-input"
                          type="text"
                          v-model="residentForm.name"
                          required
                          placeholder="Enter Name">
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-birthdate-group"
                        label="Birth Date:"
                        label-for="form-birthdate-input">
            <b-form-input id="form-birthdate-input"
                          type="text"
                          v-model="residentForm.day"
                          required
                          placeholder="Day:">
            </b-form-input>
            <b-form-input id="form-birthdate-input"
                          type="text"
                          v-model="residentForm.month"
                          required
                          placeholder="Month:">
            </b-form-input>
            <b-form-input id="form-birthdate-input"
                          type="text"
                          v-model="residentForm.year"
                          required
                          placeholder="Year:">
            </b-form-input>
          </b-form-group>

          <b-form-group id="form-email-group"
                      label="Email:"
                      label-for="form-email-input">
            <b-form-input id="form-email-input"
                          type="text"
                          v-model="residentForm.email"
                          required
                          placeholder="Enter Email">
            </b-form-input>
          </b-form-group>

          <b-button-group>
            <b-button type="submit" variant="primary">Submit</b-button>
          </b-button-group>
        </b-form>

      </b-modal>

      <!-- ADM CONTENT PART OF PAGE -->
      <b-col class="adm-content" cols="10">
        <b-container>
          <b-row align-v="start" align-h="center">

            <b-col>
              <b-card
                title="House Information"
                style="max-width: 25rem;"
                class="mb-2 house-card"
              >
                <b-card-text>
                  <p>Number: {{ houseInfo.number }}</p>
                  <p>Onwer: {{ houseInfo.onwer }}</p>
                  <p>Cond. Price: ${{ houseInfo.condominiumPrice }}</p>
                  <p>Residents: {{ houseInfo.residents }}</p>
                  <p>Fines: {{ houseInfo.fines }}</p>
                  <p>Payments: {{ houseInfo.payments }}</p>
                </b-card-text>
              </b-card>

              <b-alert :show="showMessage" dismissible>
                {{ message }}
              </b-alert>
            </b-col>

          </b-row>
        </b-container>
      </b-col>

    </b-row>
  </b-container>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Adm',
  data() {
    return {
      user_logged_in: '',
      message: '',
      showMessage: false,
      fineSelected: null,
      fineOptions: [],
      residentHouseSelected: '',
      residentsHouseOptions: [],
      houseInfo: {
        number: 1,
        onwer: '',
        residents: [],
        condominiumPrice: 0.00,
        payments: [],
        fines: [],
      },
      residentForm: {
        user: '',
        password: '',
        name: '',
        email: '',
        type: '',
        day: '',
        month: '',
        year: '',
      },
    };
  },
  methods: {
    setUser() {
      this.user_logged_in = this.$cookies.get('user');
    },
    updateHouse() {
      const payload = {
        houseNumber: this.$cookies.get('house'),
      };
      this.getHouse(payload);
    },
    getFinesOptions() {
      const path = 'http://18.231.124.87:7011/houses/fines_options';
      const payload = {
        house: this.houseInfo.number,
      };
      axios.post(path, payload)
        .then((res) => {
          this.fineOptions = res.data.fines;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    getHouse(payload) {
      const path = 'http://localhost:5000/houses/select_house';
      axios.post(path, payload)
        .then((res) => {
          this.message = res.data.message;
          this.houseInfo.number = res.data.number;
          this.houseInfo.onwer = res.data.onwer;
          this.houseInfo.condominiumPrice = res.data.condominiumP;
          this.houseInfo.residents = res.data.residents;
          this.houseInfo.fines = res.data.fines;
          this.houseInfo.payments = res.data.payments;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    registerResident(payload) {
      const path = 'http://localhost:5000/users/set_new_resident';
      axios.post(path, payload)
        .then((res) => {
          if (res.data.message === 'Resident added!') {
            this.message = res.data.message;
            this.showMessage = true;
            this.$refs.NewResidentModal.hide();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onSubmitNewResident(evt) {
      evt.preventDefault();
      const payload = {
        name: this.residentForm.name,
        email: this.residentForm.email,
        day: this.residentForm.day,
        month: this.residentForm.month,
        year: this.residentForm.year,
        house_number: this.$cookies.get('house'),
      };
      this.registerResident(payload);
      this.initForm();
    },
    makePayment(payload) {
      const path = 'http://18.231.124.87:7011/houses/make_payment';
      axios.post(path, payload)
        .then((res) => {
          if (res.data.message === 'Payment made!') {
            this.message = res.data.message;
            this.showMessage = true;
            this.$refs.makePaymentsModal.hide();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onSubmitPayment(evt) {
      evt.preventDefault();
      const payload = {
        fine: this.fineSelected,
        house_number: this.$cookies.get('house'),
      };
      this.makePayment(payload);
      this.initForm();
    },
    initForm() {
      this.residentForm.user = '';
      this.residentForm.password = '';
      this.residentForm.name = '';
      this.residentForm.email = '';
      this.residentForm.type = '';
      this.residentForm.day = '';
      this.residentForm.month = '';
      this.residentForm.year = '';
    },
  },
  mounted() {
    this.$root.$on('bv::modal::show', (bvEvent, modalId) => {
      // console.log('Modal is about to be shown', bvEvent, modalId);
      this.getFinesOptions();
    });
  },
  created() {
    this.setUser();
    this.updateHouse();
  },
};
</script>

<style scoped>

.adm-sidebar {
  padding-top: 40px;
  padding-bottom: 500px;
  background-color: rgb(230, 227, 227);
}

.menu-welcome {
  font-family: sans-serif;
  font-size: large;
  text-align: center;
  color: #f80000;
}

.menu-part-two{
  margin-top: 10px;
}

#adm-menu {
  margin-top: 20px;
}

.adm-content {
  padding-top: 50px;
}

.house-card {
  margin-left: 35%;
}

.house-select-b {
  margin-right: 90%;
}

.button-adjust {
  margin-top: 10px;
}

</style>
