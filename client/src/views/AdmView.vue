<template>
  <b-container fluid class="adm-interface">
    <b-row>

      <!-- MENU PART OF PAGE -->
      <b-col class="adm-sidebar" cols="2">
        <div class="menu-welcome"> Welcome, {{user_logged_in}}! </div>
        <div id="adm-menu">
          <b-list-group class="menu-part-one">

            <b-list-group-item button type="button" v-b-modal.new-resident-modal>
              Register New Resident
            </b-list-group-item>
            <b-list-group-item button type="button" v-b-modal.add-resident-modal>
              Add Resident to House
            </b-list-group-item>
            <b-list-group-item button type="button" v-b-modal.remove-resident-modal>
              Remove Resident of House
            </b-list-group-item>
            <b-list-group-item button type="button" v-b-modal.set-price-modal>
              Set cond. value
            </b-list-group-item>
            <b-list-group-item button type="button" v-b-modal.apply-fine-modal>
              Fine Resident
            </b-list-group-item>
          </b-list-group>
          <b-list-group class="menu-part-two">
            <b-list-group-item button>Register New Onwer</b-list-group-item>
            <b-list-group-item button>Register New Adm</b-list-group-item>
            <b-list-group-item button>Logout</b-list-group-item>
          </b-list-group>
        </div>
      </b-col>

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

          <b-form-group id="form-house-group"
                      label="House:"
                      label-for="form-house-input">
            <b-form-input id="form-house-input"
                          type="text"
                          v-model="residentForm.house_number"
                          required
                          placeholder="Enter House Number (1-6)">
            </b-form-input>
          </b-form-group>

          <b-button-group>
            <b-button type="submit" variant="primary">Submit</b-button>
          </b-button-group>
        </b-form>

      </b-modal>

      <!-- ADD RESIDENT MODAL -->
      <b-modal ref="AddResidentModal"
              id="add-resident-modal"
              title="Add Resident"
              hide-footer>
        <b-form @submit="onSubmitAddResident" class="w-100">

          <b-form-select v-model="houseSelected" :options="houseOptions"></b-form-select>
          <b-form-select v-model="residentSelected" :options="residentOptions"></b-form-select>
          <div class="mt-3">
            House Selected: {{ houseSelected }} | Resident Selected: {{ residentSelected }}
          </div>

          <b-button-group>
            <b-button type="submit" variant="primary">Submit</b-button>
          </b-button-group>
        </b-form>

      </b-modal>

      <!-- REMOVE RESIDENT MODAL -->
      <b-modal ref="RemoveResidentModal"
              id="remove-resident-modal"
              title="Remove Resident"
              hide-footer>
        <b-form @submit="onSubmitRemoveResident" class="w-100">

          <b-form-select v-model="houseSelected" :options="houseOptions"></b-form-select>
          <b-form-select
            v-model="residentHouseSelected"
            :options="residentsHouseOptions"
          >
          </b-form-select>

          <div class="mt-3">
            House Selected: {{ houseSelected }} | Resident Selected: {{ residentHouseSelected }}
          </div>

          <b-button-group>
            <b-button type="submit" variant="primary">Submit</b-button>
          </b-button-group>
        </b-form>

      </b-modal>

      <!-- SET CONDOMINIUM VALUE MODAL -->
      <b-modal ref="SetPriceModal"
              id="set-price-modal"
              title="Set Condominium Price"
              hide-footer>
        <b-form @submit="onSubmitSetPrice" class="w-100">

          <b-form-select v-model="houseSelected" :options="houseOptions"></b-form-select>
          <b-form-input v-model="newPrice" placeholder="Enter Cond. Valeu"></b-form-input>

          <div class="mt-3">
            House Selected: {{ houseSelected }} | New cond price: ${{ newPrice }}
          </div>

          <b-button-group>
            <b-button type="submit" variant="primary">Submit</b-button>
          </b-button-group>
        </b-form>

      </b-modal>

      <!-- APPLY FINE MODAL -->
      <b-modal ref="ApplyFineModal"
              id="apply-fine-modal"
              title="Apply Fine"
              hide-footer>
        <b-form @submit="onSubmitApplyFine" class="w-100">

          <b-form-select v-model="houseSelected" :options="houseOptions"></b-form-select>
          <b-form-select v-model="fineSelected" :options="fineOptions"></b-form-select>
          <b-form-input v-model="finePrice" placeholder="Enter Fine Price"></b-form-input>

          <div class="mt-3">
            House Selected: {{ houseSelected }} |
            Fine Reason: {{fineSelected}} |
            Fine price: ${{ finePrice }}
          </div>

          <b-button-group>
            <b-button type="submit" variant="primary">Submit</b-button>
          </b-button-group>
        </b-form>

      </b-modal>

      <!-- ADM CONTENT PART OF PAGE -->
      <b-col class="adm-content" cols="10">
        <b-container>
          <b-row align-v="start" align-h="center">

            <b-col cols="8">
              <b-card
                title="House Information"
                style="max-width: 25rem;"
                class="mb-2 house-card"
              >
                <b-card-text>
                  <p>Number: {{ houseSelected }}</p>
                  <p>Onwer: {{ houseInfo.onwer }}</p>
                  <p>Cond. Price: ${{ houseInfo.condominiumPrice }}</p>
                  <p>Residents: {{ houseInfo.residents }}</p>
                  <p>Fines: {{ houseInfo.fines }}</p>
                </b-card-text>
              </b-card>

              <b-alert :show="showMessage" dismissible>
                {{ message }}
              </b-alert>
            </b-col>

            <b-col cols="4">
              <div>
                <b-form-select
                  v-model="houseSelected"
                  :options="houseOptions"
                  autofocus
                >
                </b-form-select>
              </div>
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
      newPrice: 0.00,
      finePrice: 0.00,
      houseSelected: 1,
      houseOptions: [
        { value: '1', text: 'House 1' },
        { value: '2', text: 'House 2' },
        { value: '3', text: 'House 3' },
        { value: '4', text: 'House 4' },
        { value: '5', text: 'House 5' },
        { value: '6', text: 'House 6' },
      ],
      fineSelected: null,
      fineOptions: [
        { value: null, text: 'Please select an option' },
        { value: 'Delay', text: 'Delay' },
        { value: 'Noise', text: 'Noise' },
        { value: 'Dirt', text: 'Dirt' },
      ],
      residentSelected: '',
      residentOptions: [],
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
        house_number: '',
      },
    };
  },
  watch: {
    houseSelected() {
      this.updateHouse();
    },
  },
  methods: {
    setUser() {
      this.user_logged_in = this.$cookies.get('user');
    },
    updateHouse() {
      const payload = {
        houseNumber: this.houseSelected,
      };
      this.getHouse(payload);
    },
    getResidentsOptions() {
      const path = 'http://172.31.2.180:5000/users/all_residents_options';
      axios.get(path)
        .then((res) => {
          this.residentOptions = res.data.residents;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    getResidentsOfHouseOptions() {
      const path = 'http://172.31.2.180:5000/users/residents_of_house_options';
      const payload = {
        house: this.houseSelected,
      };
      axios.post(path, payload)
        .then((res) => {
          this.residentsHouseOptions = res.data.residents;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    getHouse(payload) {
      const path = 'http://172.31.2.180:5000/houses/select_house';
      axios.post(path, payload)
        .then((res) => {
          this.message = res.data.message;
          this.houseInfo.number = res.data.number;
          this.houseInfo.onwer = res.data.onwer;
          this.houseInfo.condominiumPrice = res.data.condominiumP;
          this.houseInfo.residents = res.data.residents;
          this.houseInfo.fines = res.data.fines;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    registerResident(payload) {
      const path = 'http://172.31.2.180:5000/users/set_new_resident';
      axios.post(path, payload)
        .then((res) => {
          if (res.data.message === 'Resident added!') {
            this.message = res.data.message;
            this.showMessage = true;
            this.residentForm.user = res.data.user;
            this.residentForm.password = res.data.password;
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
        house_number: this.house_number,
      };
      this.registerResident(payload);
      this.initForm();
    },
    addResident(payload) {
      const path = 'http://172.31.2.180:5000/users/add_new_resident';
      axios.post(path, payload)
        .then((res) => {
          if (res.data.message === 'Resident added to house!') {
            this.message = res.data.message;
            this.$refs.AddResidentModal.hide();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onSubmitAddResident(evt) {
      evt.preventDefault();
      const payload = {
        house: this.houseSelected,
        resident: this.residentSelected,
      };
      this.addResident(payload);
      this.initForm();
    },
    removeResidentFromHouse(payload) {
      const path = 'http://172.31.2.180:5000/users/remove_resident_house';
      axios.post(path, payload)
        .then((res) => {
          if (res.data.message === 'Resident removed of house!') {
            this.message = res.data.message;
            this.$refs.RemoveResidentModal.hide();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onSubmitRemoveResident(evt) {
      evt.preventDefault();
      const payload = {
        house: this.houseSelected,
        resident: this.residentHouseSelected,
      };
      this.removeResidentFromHouse(payload);
      this.initForm();
    },
    setCondPrice(payload) {
      const path = 'http://172.31.2.180:5000/houses/set_price';
      axios.post(path, payload)
        .then((res) => {
          if (res.data.message === 'New Price Updated!') {
            this.message = res.data.message;
            this.$refs.SetPriceModal.hide();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onSubmitSetPrice(evt) {
      evt.preventDefault();
      const payload = {
        house: this.houseSelected,
        price: this.newPrice,
      };
      this.setCondPrice(payload);
    },
    applyFine(payload) {
      const path = 'http://172.31.2.180:5000/houses/apply_fine';
      axios.post(path, payload)
        .then((res) => {
          if (res.data.message === 'Fine Applied!') {
            this.message = res.data.message;
            this.$refs.ApplyFineModal.hide();
          }
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    onSubmitApplyFine(evt) {
      evt.preventDefault();
      const payload = {
        house: this.houseSelected,
        reason: this.fineSelected,
        price: this.finePrice,
      };
      this.applyFine(payload);
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
      console.log('Modal is about to be shown', bvEvent, modalId);
      this.getResidentsOptions();
      this.getResidentsOfHouseOptions();
      console.log(this.residentsHouseOptions);
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

</style>
