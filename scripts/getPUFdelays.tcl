# set target_nets [get_nets -hierarchical -regexp {.*puf_inst.*dl.*}]
set target_nets [get_nets -regexp -hierarchical {.*puf_loop.*dl.*in0.*|.*puf_loop.*dl.*out.*|.*puf_loop.*dl.*reset.*|.*puf_loop.*dl.*OUT.*|.*puf_loop.*dl.*P0.*}]


# set target_pins [get_pins -of $target_cells]

# set p_nets [get_nets -of $target_pins]
set fh [open "H:/PUF/PUF_manualPR/Nx_PR06sync.csv" w]

puts $fh "Net Name, To Pin, Delay Type, Delay (ps)"

# foreach cell $target_cells {
foreach net $target_nets {
    set net_delays [get_net_delays -of_objects $net]
    foreach delay $net_delays {
        set d_max [get_property SLOW_MAX $delay]
        set to_pin [get_property TO_PIN $delay]

        puts $fh "$net,$to_pin,NetDelay,$d_max"
    }
    
    # set net_delay [get_property SLOW_MAX $delays]
    # set pin_delay [get_property -max DELAY_VALUE $pin]
    
}
# }

close $fh



