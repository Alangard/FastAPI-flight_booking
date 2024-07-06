<template>

<!-- <v-skeleton-loader
    :loading="loading_tickets"
    class="mx-auto w-100 mb-3 px-3 ticket"
    elevation="12"
    type="table-heading, list-item-three-line, button, button">
</v-skeleton-loader> -->


<v-card class="mb-3 px-3 ticket" v-show="!loading_tickets">

    <div class="ticket_top d-flex flex-row justify-start align-center">
        <v-img class="flex-0-0 my-2 mr-2" width="27" :aspect-ratio="1"  src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"></v-img>
        <div>British Airway</div>
    </div>
    <div class="ticket_main mb-3">
        <div class="d-flex flex-row justify-space-between align-center">
            <h2>23:55</h2>
            <span class="text-body-2 text-medium-emphasis">1 ч 30 м</span>
            <h2>01:25</h2>
        </div>
        <div class="time_divider mt-2 mb-3"></div>
        <div class="d-flex flex-row justify-space-between align-center">
            <div class="from_info d-flex flex-column align-start">
                <span class="text-body-2 text-medium-emphasis">12 Jul, Fri</span>
                <span class="text-body-2">Airport code</span>
                <span class="text-body-2 text-medium-emphasis">Town from</span>
            </div>
            <div class="to_info d-flex flex-column align-end">
                <span class="text-body-2 text-medium-emphasis">13 Jul, Sat</span>
                <span class="text-body-2">Airport code</span>
                <span class="text-body-2 text-medium-emphasis">Town to</span>
            </div>
        </div> 
    </div>
    <v-divider></v-divider>
    <div class="ticket_bot"></div>

    <v-card 
        class="d-flex flex-row align-center justify-space-between px-4"
        rounded="lg" 
        variant="tonal" 
        height="35">
        <div class="d-flex flex-row align-center">
            <h4 class="mr-3">Luggage 25 kg</h4>
            <h4 class="text-orange-darken-3">+$30</h4>
        </div>

        <v-switch 
            v-model="with_luggage"
            color="orange-darken-3"
            hide-details
        ></v-switch>
    </v-card>

    <div class='d-flex flex-row justify-space-between align-center my-2'>
        <div class="d-flex flex-column">
            <h2>${{with_luggage ? 546 + 30 : 546}}</h2>
            <span class="text-body-2">{{with_luggage ? 'with': 'without'}} luggage</span>
            
        </div>
        <v-btn
            color="orange-darken-3"
            text="Book now"
            variant="tonal"
            @click="save_passangers_count_and_grade">
        </v-btn>
    </div>
</v-card>


</template>
<script>
export default {
    components: {},
    data () {
        return {
            loading_tickets: false,
            with_luggage: false
        }
    }
}
</script>
<style lang='css' scoped>
.time_divider {
    border-bottom: 1px solid var(--grey-lighten-2, #c3cfdf);
    position: relative;
    padding: 0 5px;
}

.time_divider::after,
.time_divider::before{
    content: "";
    position: absolute;
    top: -2px;
    left: 0;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background-color: var(--grey-lighten-2, #c3cfdf);
}

.time_divider::after{
    left: calc(100% - 5px);
}
</style>