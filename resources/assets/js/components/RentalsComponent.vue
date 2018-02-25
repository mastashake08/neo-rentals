<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card card-default">
                    <div class="card-header">Rentals</div>

                    <div class="card-body">
                      <ul>
                        
                      </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        mounted() {
            console.log('Component mounted.')
        },
        data() {
          return {
          rentals : [],
          description:"",
          selectedRental: {},
          scriptBuilder: {}

        }
        },
        created(){
          this.scriptBuilder = Neon.default.create.scriptBuilder()

        },
        methods:{
          addClaim: function(){
            var that = this
            axios.post('/api/claim',{rental_id:that.selectedRental.id}).then(function(data){
              /*
              Invoke smart contract function to add claim to blockchain
              */
            })
          }
        }
    }
</script>
