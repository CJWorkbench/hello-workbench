from pandas.api.types import is_numeric_dtype


def render(table, params, columns):
    colname = params['colname']
    factor  = params['factor']

    # If no column is selected, do nothing. Workbench's convention is modules 
    # do not alter their input when waiting for parameters to be filled out
    if not colname:
        return table

    # Don't worry about table[colname] not existing. Workbench guarantees it
    # exists.
    
    # If the column is not a number, return an error message
    # see https://github.com/CJWorkbench/cjworkbench/wiki/Column-Types
    if columns[colname].type != 'number':
    	return "Please select a Number column"

    # Modules may alter their input in place, if desired
    table[colname] *= factor
    return table
