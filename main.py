# role = "service_a"
# store = ParameterStore()
# foo_id = store.create_parameter(role, "someParamValue")
# store.get_parameter(role, foo_id) -> "someParamValue"


# Any calls made to this parameter store are authenticated, assume role is valid.
class ParameterStore:
    def __init__(self) -> None:
        self.parameter_id = 0    
        self.parameter_store = {}  # key - role, value - list of param ids  {'roleA':{'param_id1: param_val}'}  
        
    def create_parameter(self, role: str, value: str) -> str:
        """Creates a parameter and returns the parameter id"""
        self.parameter_id += 1
        if role not in self.parameter_store:
            self.parameter_store[role] = {}

        self.parameter_store[role][self.parameter_id] = value
        
        return self.parameter_id

    def get_parameter(self, role: str, parameter_id: str) -> str:
        """Returns the parameter value, if the role can access the parameter."""
        if role not in self.parameter_store:
            raise Exception("Role not able to access parameter !!")
        try: 
            result = self.parameter_store[role][parameter_id]
        except(KeyError):
            return "Role not able to access parameter"
        
        return result

    def find_parameters(self, role: str) -> Iterable[str]:
        """Returns a list of parameter ids that the given role can access."""
        param_id_list = []
        try:
            param_id_list.append(self.parameter_store[role].keys())
        except(KeyError):
            return "Role not able to access parameter"
        return param_id_list

