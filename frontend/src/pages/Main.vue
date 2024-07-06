<template>
   
    

        
        <v-card class="mx-5 w-100" max-width="750px" >
            <v-toolbar color="surface" height="0">
            <template v-slot:extension>
                <v-tabs v-model="tabs" color="orange-darken-3" grow>
                    <v-tab :value="1">
                        <v-icon icon="mdi-airplane"></v-icon> Flight
                    </v-tab>

                    <v-tab :value="2">
                        <v-icon icon="mdi-bed"></v-icon>Hotel
                    </v-tab>

                    <v-tab :value="3">
                        <v-icon icon="mdi-bag-suitcase"></v-icon>Events
                    </v-tab>
                </v-tabs>
            </template>
            </v-toolbar>

            <v-tabs-window v-model="tabs">
            <v-tabs-window-item
                v-for="i in 3" :key="i" :value="i">
                <v-card>
                <v-card-text v-if="i == 1">
                    <v-radio-group v-model="flight_type" inline>
                      <v-radio class="mr-2" label="One Way" value="one" color="orange-darken-3"></v-radio>
                      <v-radio label="Round Way" value="round" color="orange-darken-3"></v-radio>
                    </v-radio-group>
                    <v-container class="city_container d-flex justify-space-between pa-0 ">
                      <v-autocomplete
                          class="w-100"
                          v-model="from_city"
                          label="From"
                          variant="solo"
                          density="comfortable"
                          menu-icon=""
                          :items="cities"
                          return-object 
                          item-title="state" 
                          item-value="abbr">
                      </v-autocomplete>

                    
                      <div class="swap_city_btn mx-2">
                          <v-btn 
                          @click="[from_city, to_city] = [to_city, from_city]"
                          icon=""
                          density="comfortable" 
                          size="large">
                          <v-icon icon="mdi-swap-horizontal"  color="orange-darken-3"></v-icon>
                          </v-btn>
                      </div>

                        <v-autocomplete
                          class="w-100"
                          v-model="to_city"
                          label="To"
                          variant="solo"
                          density="comfortable"
                          menu-icon=""
                          :items="cities"
                          return-object 
                          item-title="state" 
                          item-value="abbr">
                        </v-autocomplete>

                    </v-container>

                    <v-form>
                    <v-container class="d-flex justify-space-between pa-0" >
                        <v-date-input 
                        v-model="datepicker_model"
                        class="w-100"
                        :label="flight_type == 'round' ? 'Depart - Return Dates' : 'Depart Date'" 
                        :prepend-inner-icon="flight_type == 'round' ? '$calendar': 'mdi-calendar-arrow-right'"
                        :multiple="flight_type == 'round' ? 'range': 'false'"
                        prepend-icon="" 
                        variant="solo"
                        density="comfortable"
                        clearable>
                        </v-date-input>
                    </v-container>
                    </v-form>

                    <v-textarea 
                    v-model="passangers_count_and_grade" 
                    label="Passanger count and flight class" 
                    variant="solo"
                    append-inner-icon="$dropdown"
                    auto-grow='true'
                    rows="1"
                    @click="passangers_count_and_grade_model = true">
                    </v-textarea>


                    
                </v-card-text>

                <v-card-actions>
                    <v-btn variant="tonal" @click="search_tickets" color="orange-darken-3" block>Search</v-btn>
                </v-card-actions>

                </v-card>
            </v-tabs-window-item>
            </v-tabs-window>
        </v-card>



    <v-dialog 
    v-model="passangers_count_and_grade_model" 
    width="auto" 
    min-width="400px" 
    height="100vh" 
    transition="dialog-bottom-transition"
  >
    <v-card class="mx-6 mt-2" max-width="750" min-width="300">
      <v-card-title class="d-flex flex-row align-center justify-space-between">
        Passangers Count
        <v-btn density="compact" icon="mdi-window-close" @click="passangers_count_and_grade_model = false"></v-btn>
      </v-card-title>
      <v-list lines="two">
        <v-list-item class="d-flex flex-row justify-space-between" title="Adults" subtitle="12 years and older">
          <template v-slot:append>
            <div class="d-flex flex-row align-center">
              <v-btn class="mr-3" icon="" density="comfortable" size="small" @click="passanger_count.adults += 1">
                <v-icon icon="mdi-plus-thick"  color="orange-darken-3"></v-icon>
              </v-btn>
              <h4>{{ passanger_count.adults }}</h4>
              <v-btn class="ml-3" icon="" density="comfortable" size="small" :disabled="passanger_count.adults == 0" @click="passanger_count.adults -= 1">
                <v-icon icon="mdi-minus-thick"  color="orange-darken-3"></v-icon>
              </v-btn>
            </div>
          </template>
        </v-list-item>

        <v-divider></v-divider>

        <v-list-item class="d-flex flex-row justify-space-between" title="Children" subtitle="2 to 11 years">
          <template v-slot:append>
            <div class="d-flex flex-row align-center">
              <v-btn class="mr-3" icon="" density="comfortable" size="small" @click="passanger_count.children += 1">
                <v-icon icon="mdi-plus-thick"  color="orange-darken-3"></v-icon>
              </v-btn>
              <h4>{{ passanger_count.children }}</h4>
              <v-btn class="ml-3" icon="" density="comfortable" size="small" :disabled="passanger_count.children == 0" @click="passanger_count.children -= 1">
                <v-icon icon="mdi-minus-thick"  color="orange-darken-3"></v-icon>
              </v-btn>
            </div>
          </template>
        </v-list-item>

        <v-divider></v-divider>

        <v-list-item class="d-flex flex-row justify-space-between" title="Babies" subtitle="Under 2 years">
          <template v-slot:append>
            <div class="d-flex flex-row align-center">
              <v-btn class="mr-3" icon="" density="comfortable" size="small" @click="passanger_count.babies += 1">
                <v-icon icon="mdi-plus-thick"  color="orange-darken-3"></v-icon>
              </v-btn>
              <h4>{{ passanger_count.babies }}</h4>
              <v-btn class="ml-3" icon="" density="comfortable" size="small" :disabled="passanger_count.babies == 0" @click="passanger_count.babies -= 1">
                <v-icon icon="mdi-minus-thick"  color="orange-darken-3"></v-icon>
              </v-btn>
            </div>
          </template>
        </v-list-item>
      </v-list>

      <v-card-title>Flight Grade</v-card-title>
      <v-list lines="one">
        <v-radio-group v-model="flight_grade" inline>
          <v-list-item class="d-flex flex-row justify-space-between w-100 pr-1" title="Economy">
            <template v-slot:append>
              <v-radio value="economy" color="orange-darken-3"></v-radio>
            </template>
          </v-list-item>
        
          <v-divider></v-divider>

          <v-list-item class="d-flex flex-row justify-space-between w-100 pr-1" title="Comfort">
            <template v-slot:append>
              <v-radio value="сomfort" color="orange-darken-3"></v-radio>
            </template>
          </v-list-item>

          <v-divider></v-divider>

          <v-list-item class="d-flex flex-row justify-space-between w-100 pr-1" title="Business">
            <template v-slot:append>
              <v-radio value="business" color="orange-darken-3"></v-radio>
            </template>
          </v-list-item>

          <v-divider></v-divider>

          <v-list-item class="d-flex flex-row justify-space-between w-100 pr-1" title="First Class">
            <template v-slot:append>
              <v-radio value="first_class" color="orange-darken-3"></v-radio>
            </template>
          </v-list-item>
        </v-radio-group>
      </v-list>

      <v-card-actions class="pt-0">
        <v-btn
          color="orange-darken-3"
          text="Submit"
          variant="tonal"
          block
          @click="save_passangers_count_and_grade"
        ></v-btn>
      </v-card-actions>

    </v-card>
    </v-dialog>
</template>
  
<script>
export default {
    components: {},
    data () {
      return {
        tabs: null,
        flight_type: 'one',
        cities: [
          { state: 'Florida', abbr: 'FL' },
          { state: 'Georgia', abbr: 'GA' },
          { state: 'Nebraska', abbr: 'NE' },
          { state: 'California', abbr: 'CA' },
          { state: 'New York', abbr: 'NY' },
        ],
        from_city: { state: 'Florida', abbr: 'FL' },
        to_city: { state: 'New York', abbr: 'NY' },
        datepicker_model: null,
        passangers_count_and_grade: '',
        passangers_count_and_grade_model: false,
        passanger_count: {'adults': 0, 'children': 0, 'babies': 0},
        flight_grade: 'economy',

      }
    },

    methods: {
      save_passangers_count_and_grade(){
        let result_string = ''
      
        for (const [key, value] of Object.entries(this.passanger_count)) {
            if(value != 0){
              result_string += value + " " + key +', '
              console.log(result_string)
            }
        }

        if(result_string.length == 0){
          result_string = '0 passangers '
        }

        this.passangers_count_and_grade += result_string.replace(/,\s*$/, '') + ' in ' + this.flight_grade + ' class'
        this.passangers_count_and_grade_model = false;
      },

      search_tickets(){
        this.expand = ! this.expand
      },
    },

    watch: {
    flight_type(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.datepicker_model = null;
      }
    }
  },

}
</script>
  
  <style lang='css' scoped>
  
  .city_container{
    position: relative;
  }

  
  .v-picker {
    max-width: none !important;
  }
  
 
  </style>