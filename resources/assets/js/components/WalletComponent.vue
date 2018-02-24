<template>
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-md-8">
                <div class="card card-default">
                    <div class="card-header">My Wallet</div>

                    <div class="card-body">
                        <b>{{neoAccount}}</b>
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
          privateKey : null,
          wif: null,
          neoAccount: {},
          publicKey: null,
          address: null,

        }
        },
        created(){
          this.createNeoAccount()


        },
        methods:{
          createNeoAccount: function(){
            this.privateKey = Neon.default.create.privateKey();

            this.wif = Neon.default.get.WIFFromPrivateKey(this.privateKey)
            this.neoAccount = Neon.default.create.account(this.privateKey)
            this.publicKey = this.neoAccount.publicKey
            this.address = this.neoAccount.address
            /*
            // Encryption / Decryption
            const encrypted = Neon.encrypt.privateKey(privateKey, 'myPassword')
            const decrypted = Neon.decrypt.privateKey(encrypted, 'myPassword')

            // Verify keys
            Neon.is.wif(wif) // true
            Neon.is.publicKey('randomphrase') // false

            // Transaction signing
            const signature = Neon.create.signature(tx, privateKey)
            */

          },

        }
    }
</script>
