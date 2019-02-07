<template>
<div class="form-group" :class="{ 'has-error': error }">
  <label v-if="label" class="control-label" :class="labelWidth">{{ label }}</label>
  <div :class="inputWidth">
    <input :type="type"
           class="form-control"
           ref="textfield"
           :placeholder="placeholder"
           @input="updateValue()"
           :value="value"
           >
    <span v-if="error" class="help-block">
      <p v-for="(msg, index) in errorMessages" :key="`error-${index}`">{{ msg }}</p>
    </span>
  </div>
</div>
</template>

<script>
export default {
    name: 'm-textfield',
    props: {
        error: {
            type: Boolean,
            default: false
        },
        errorMessages: Array,
        label: String,
        placeholder: String,
        type: {
            type: String,
            default: 'text'
        },
        labelWidth: {
            type: String,
            default: 'col-sm-3'
        },
        inputWidth: {
            type: String,
            default: 'col-sm-7'
        },
        value: { required: false }
    },
    methods: {
        updateValue () {
            this.$emit('input', this.$refs.textfield.value)
        }
    }
}
</script>
