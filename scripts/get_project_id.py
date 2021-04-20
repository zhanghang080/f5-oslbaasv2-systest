import os
import sys
fp = os.path.abspath(__file__)

sys.path.append(os.path.join(os.path.dirname(fp), './tools'))
from libs import lbaasv2_helper as lb


os_project_name = os.environ["OS_PROJECT_NAME"]
helper = lb.LBaasV2Helper()
os_project_id = helper.get_project_id(os_project_name)
print(os_project_id)
if os_project_id is None:
    sys.exit(1)
sys.exit(0)