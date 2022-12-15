import yaml

with open('netplan.yaml', 'r') as f:
    config = yaml.load(f, yaml.SafeLoader)

(config['network']['ethernets']['enp0s25']
       ['nameservers']['addresses'][1]) = '8.8.8.8'

print(yaml.dump(config, sort_keys=False))

exit()
with open('netplan_out.yaml', 'w') as f:
    f.write(yaml.dump(config, sort_keys=False))
