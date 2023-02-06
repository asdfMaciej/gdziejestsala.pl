
<script lang="ts">
// @ts-ignore
import { QrcodeStream } from 'qrcode-reader-vue3'
export default {
    components: { QrcodeStream },

    data() {
        return {
            result: '',
            error: '',
            camera: 'rear',

            noRearCamera: false,
            noFrontCamera: false
        }
    },

    methods: {
        switchCamera() {
            switch (this.camera) {
                case 'front':
                    this.camera = 'rear'
                    break
                case 'rear':
                    this.camera = 'front'
                    break
            }
        },

        onDecode(result: any) {
            this.result = result;

            // Get capturing group for /route/(1234)/ with optional trailing slash
            const route_regex = /.*\/route\/(\d+)\/?/;
            const match = result.match(route_regex);
            const matched_id = (match && match.length > 1) ? match[1] : null;

            if (matched_id !== null) {
                console.log(`matched ${matched_id}`);
                this.$emit('match', matched_id);
            }
        },

        async onInit(promise: any) {
            try {
                await promise
            } catch (error: any) {
                if (error.name === 'NotAllowedError') {
                    this.error = "ERROR: you need to grant camera access permission"
                } else if (error.name === 'NotFoundError') {
                    this.error = "ERROR: no camera on this device"
                } else if (error.name === 'NotSupportedError') {
                    this.error = "ERROR: secure context required (HTTPS, localhost)"
                } else if (error.name === 'NotReadableError') {
                    this.error = "ERROR: is the camera already in use?"
                } else if (error.name === 'StreamApiNotSupportedError') {
                    this.error = "ERROR: Stream API is not supported in this browser"
                } else if (error.name === 'InsecureContextError') {
                    this.error = 'ERROR: Camera access is only permitted in secure context. Use HTTPS or localhost rather than HTTP.';
                } else {
                    console.log(`ERROR: Camera error (${error.name})`);
                }

                const triedFrontCamera = this.camera === 'front'
                const triedRearCamera = this.camera === 'rear'

                const cameraMissingError = error.name === 'OverconstrainedError'

                if (triedRearCamera && cameraMissingError) {
                    this.noRearCamera = true
                }

                if (triedFrontCamera && cameraMissingError) {
                    this.noFrontCamera = true
                }

                if (cameraMissingError) {
                    this.switchCamera();
                }
            }
        }
    }
}
</script>

<template>
    <div>
        <p class="error">{{ error }}</p>

        <p class="decode-result"></p>

        <qrcode-stream :camera="camera" @decode="onDecode" @init="onInit">
            <button @click="switchCamera">
                <img src="/assets/camera-switch.svg" alt="switch camera" width="40"> <!-- TODO: proper assets link -->
            </button>
        </qrcode-stream>
    </div>
</template>


<style scoped>
.error {
    font-weight: bold;
    color: red;
}

button {
    position: absolute;
    left: 10px;
    top: 10px;
    background: none;
    border: none;
    width: auto;
}
</style>