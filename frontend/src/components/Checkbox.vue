<template>
<div class="form-group">
  <div class="col-sm-offset-3 col-sm-7">
    <div class="checkbox">
      <label>
        <input type="checkbox"
               :checked="value"
               ref="checkbox"
               @input="updateValue()"> {{ label }}
      </label>
    </div>
  </div>
</div>
</template>

<script>
export default {
    props: {
        label: String,
        value: Boolean
    },
    methods: {
        updateValue () {
            this.$emit('input', this.$refs.checkbox.checked)
        }
    }
}
</script>
