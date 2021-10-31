// Blockly.defineBlocksWithJsonArray([{
//     "type": "forward",
//     "message0": "Move Forward %1",
//     "args0": [
//         {
//             "type": "input_value",
//             "name": "hi"
//         }
//     ],
//     "inputsInline": false,
//     "colour": 120,
//     "tooltip": "",
//     "helpUrl": ""
// }]);

Blockly.Blocks['testblock'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Helloooo");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['forward'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Move Forward");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(120);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['turn'] = {
    init: function () {
        this.appendDummyInput()
            .appendField("Turn")
            .appendField(new Blockly.FieldDropdown([["Left 90°", "left90"], ["Right 90°", "right90"]]), "NAME");
        this.setPreviousStatement(true, null);
        this.setNextStatement(true, null);
        this.setColour(330);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['repeatuntilend'] = {
    init: function () {
        this.appendStatementInput("NAME")
            .setCheck(null)
            .appendField("Repeat Until End");
        this.setPreviousStatement(true, null);
        this.setColour(230);
        this.setTooltip("");
        this.setHelpUrl("");
    }
};

Blockly.Blocks['print'] = {
    init: function() {
      this.appendDummyInput()
          .appendField("print")
          .appendField(new Blockly.FieldTextInput(""), "");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(0);
   this.setTooltip("");
   this.setHelpUrl("");
    }
  };

Blockly.JavaScript['forward'] = function (block) {
    // TODO: Assemble JavaScript into code variable.
    var code = '...;\n';
    return code;
};

Blockly.JavaScript['turn'] = function (block) {
    var dropdown_name = block.getFieldValue('NAME');
    // TODO: Assemble JavaScript into code variable.
    var code = '...;\n';
    return code;
};

Blockly.JavaScript['repeatuntilend'] = function (block) {
    var statements_name = Blockly.JavaScript.statementToCode(block, 'NAME');
    // TODO: Assemble JavaScript into code variable.
    var code = '...;\n';
    return code;
};

Blockly.JavaScript['print'] = function(block) {
    // TODO: Assemble JavaScript into code variable.
    var code = '...;\n';
    return code;
  };