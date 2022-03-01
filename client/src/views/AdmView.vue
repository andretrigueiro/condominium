<template>
  <b-container fluid class="adm-interface">
    <b-row>

      <b-col class="adm-sidebar" cols="2">
        <div class="menu-welcome"> Welcome, {{user_logged_in}}! </div>
        <div id="adm-menu">
          <b-list-group class="menu-part-one">
            <b-list-group-item button>Register New Resident</b-list-group-item>
            <b-list-group-item button>Remove Resident</b-list-group-item>
            <b-list-group-item button>Set cond. value</b-list-group-item>
            <b-list-group-item button>Fine Resident</b-list-group-item>
          </b-list-group>
          <b-list-group class="menu-part-two">
            <b-list-group-item button>Register New Onwer</b-list-group-item>
            <b-list-group-item button>Register New Adm</b-list-group-item>
            <b-list-group-item button>Logout</b-list-group-item>
          </b-list-group>
        </div>
      </b-col>

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
                  <p>Number: {{ houseInfo.number }}</p>
                  <p>Onwer: {{ houseInfo.onwer }}</p>
                  <p>Residents: {{ houseInfo.residents }}</p>
                  <p>Cond. Price: ${{ houseInfo.condominiumPrice }}</p>

                </b-card-text>
              </b-card>
            </b-col>

            <b-col cols="4">
              <b-dropdown id="dropdown-1"
                text="Select house"
                variant="secondary"
                class="house-select-b">
                  <b-dropdown-item-button value=1 v-model="houseNumber">
                    House 1
                  </b-dropdown-item-button>
                  <b-dropdown-item-button value=2 v-model="houseNumber">
                    House 2
                  </b-dropdown-item-button>
                  <b-dropdown-item-button>House 3</b-dropdown-item-button>
                  <b-dropdown-item-button>House 4</b-dropdown-item-button>
                  <b-dropdown-item-button>House 5</b-dropdown-item-button>
                  <b-dropdown-item-button>House 6</b-dropdown-item-button>
              </b-dropdown>
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
      houseNumber: 1,
      houseInfo: {
        number: 1,
        onwer: 'Jose',
        residents: [],
        condominiumPrice: 0.00,
        debts: [],
        payments: [],
        fines: [],
      },
    };
  },
  methods: {
    setUser() {
      this.user_logged_in = this.$cookies.get('user');
    },
    setHouse(houseNumber) {
      const path = 'http://localhost:5000/users/houses';
      axios.post(path, houseNumber)
        .then((res) => {
          this.houseInfo.number = res.data.number;
          this.houseInfo.onwer = res.data.onwer;
          this.houseInfo.residents = res.data.residents;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
    },
    // houseNumberSelection(evt) {
    //   pa
    // },
  },
  created() {
    this.setUser();
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
