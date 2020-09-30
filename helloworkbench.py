def render(table, params, *, input_columns):
    colname = params["colname"]
    factor = params["factor"]

    # If no column is selected, do nothing. By convention, Workbench modules
    # should output their input until enough parameters are supplied.
    if not colname:
        return table

    # Don't worry about table[colname] not existing. Workbench guarantees it
    # exists.

    # If the column is not a number, return an error message
    # see https://github.com/CJWorkbench/cjworkbench/wiki/Column-Types
    if input_columns[colname].type != "number":
        return "Please select a Number column"

    # Modules may alter their input in place, if desired
    table[colname] *= factor
    return table
