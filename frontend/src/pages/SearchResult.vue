<template>
    <div class="d-flex flex-column w-100 px-5" style="max-width: 750px;">
        <v-card class="mb-6">
            <v-card-text>
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
                        item-value="abbr"
                    ></v-autocomplete>

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
                        item-value="abbr"
                    ></v-autocomplete>

                </v-container>      
            </v-card-text>

            <v-card-actions>
                <v-btn variant="tonal" @click="search_tickets" color="orange-darken-3" block>Search</v-btn>
            </v-card-actions>
        </v-card>

        
        <TicketList v-for="id in 3" :key="id"></TicketList>
    </div>
</template>

<script>
import TicketList from '@/components/TicketList.vue'
export default {
    components: {
        TicketList
    },
    data () {
        return {
            flight_type: 'one',
        }
    }
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