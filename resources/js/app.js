require('./bootstrap');
import { createApp } from 'vue'
import HeaderComponent from './components/HeaderComponent.vue'

createApp({
    components:{
        HeaderComponent
    }
}).mount('#app')
